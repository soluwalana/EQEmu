import json
import re
import time
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup
from bs4.element import AttributeValueList

BASE = "https://www.ign.com"
ROOT = f"{BASE}/wikis/everquest/"
OUTPUT = Path("everquest_lore.jsonl")

USER_AGENT = "EverQuestLoreResearchBot/1.0"
DELAY = 2.0
MAX_PAGES = 2000

LORE_TERMS = {
    "lore",
    "history",
    "story",
    "legend",
    "myth",
    "god",
    "gods",
    "deity",
    "pantheon",
    "dragon",
    "empire",
    "timeline",
    "norrath",
    "creation",
    "war",
    "race",
    "faction",
    "religion",
}

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})


def normalize_url(url: str | AttributeValueList) -> str | None:
    if isinstance(url, AttributeValueList):
        url = str(url)

    absolute = urljoin(BASE, url)
    parts = urlsplit(absolute)

    if parts.netloc.lower() != "www.ign.com":
        return None

    path = re.sub(r"/+", "/", parts.path)

    if not path.startswith("/wikis/everquest/"):
        return None

    if re.search(r"\.(jpg|png|gif|pdf|webp)$", path, re.IGNORECASE):
        return None

    return urlunsplit(("https", "www.ign.com", path, "", ""))


def extract_article(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "lxml")

    title_node = soup.select_one("h1")
    title = (
        title_node.get_text(" ", strip=True)
        if title_node
        else soup.title.get_text(" ", strip=True) if soup.title else ""
    )

    # Candidate containers, ordered from specific to generic.
    selectors = [
        "article",
        '[itemprop="articleBody"]',
        ".wiki-page-content",
        ".article-content",
        "main",
    ]

    content = next(
        (node for sel in selectors if (node := soup.select_one(sel))),
        None,
    )

    if content is None:
        return {
            "url": url,
            "title": title,
            "content": "",
            "headings": [],
            "links": [],
        }

    # Remove non-article elements.
    for node in content.select(
        "script, style, nav, footer, aside, "
        "form, button, noscript, "
        '[role="navigation"], [class*="advert"]'
    ):
        node.decompose()

    blocks = []
    headings = []

    for node in content.select("h1, h2, h3, h4, p, li"):
        text = node.get_text(" ", strip=True)

        if not text:
            continue

        if node.name.startswith("h"):
            headings.append(text)
            blocks.append(f"\n## {text}\n")
        else:
            blocks.append(text)

    # Internal wiki references.
    links = set()

    for a in content.select("a[href]"):
        target = normalize_url(a["href"])
        if target and target != url:
            links.add(target)

    content_text = "\n\n".join(blocks)

    return {
        "url": url,
        "title": title,
        "headings": headings,
        "content": content_text,
        "links": sorted(links),
    }


def is_lore(article: dict) -> bool:
    # Initial heuristic, not a definitive classification.
    text = " ".join(
        [
            article["title"],
            *article["headings"],
            urlsplit(article["url"]).path.split("/")[-1],
        ]
    ).lower()

    return True

    return any(re.search(rf"\b{re.escape(term)}\b", text) for term in LORE_TERMS)


def crawl() -> None:

    queue = deque([ROOT])
    seen = set()

    pages = 0
    lore_pages = 0

    with OUTPUT.open("w", encoding="utf-8") as out:
        while queue and pages < MAX_PAGES:
            url = queue.popleft()

            if url in seen:
                continue

            seen.add(url)

            time.sleep(DELAY)

            try:
                response = session.get(url, timeout=30)
                response.raise_for_status()

                if "text/html" not in response.headers.get("Content-Type", ""):
                    continue

                article = extract_article(response.text, url)

            except requests.RequestException as exc:
                print("FAILED:", url, exc)
                continue

            pages += 1

            # Discover links from the original page, including
            # sidebar/navigation links not in the article itself.
            soup = BeautifulSoup(response.text, "lxml")

            for anchor in soup.select("a[href]"):
                target = normalize_url(anchor["href"])
                if target and target not in seen:
                    queue.append(target)

            if not article["content"]:
                print("EMPTY:", url)
                continue

            article["is_lore"] = is_lore(article)

            if article["is_lore"]:
                lore_pages += 1
                out.write(json.dumps(article, ensure_ascii=False) + "\n")
                out.flush()
                print(f"LORE [{lore_pages}]: {article['title']}")
            else:
                print(f"SKIP: {article['title']}")

    print(f"\nVisited {pages} pages")
    print(f"Saved {lore_pages} lore articles")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    crawl()
