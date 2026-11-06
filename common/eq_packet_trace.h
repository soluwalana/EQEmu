#pragma once
// EQEmu debug-only application-packet recorder; POSIX/Linux. Header-only.
// Format: uint32 LE frame_length, then <QBBHHI> and opcode, peer, payload.
// Set EQEMU_PACKET_TRACE=/tmp/eqtrace to produce /tmp/eqtrace.<pid>.bin

#include "common/eq_packet.h"
#include "common/opcodemgr.h"
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <fcntl.h>
#include <string>
#include <string_view>
#include <unistd.h>
#include <vector>

namespace PacketTrace {

inline void Record(const EQApplicationPacket *p, bool server_to_client,
                   bool client_layout, std::string_view peer) {
  if (!p || (p->size && !p->pBuffer) || p->size > 8u * 1024u * 1024u)
    return;

  // Separate per-process files prevent concurrent zone processes from
  // interleaving their records. Disabled by default.
  static const int fd = [] {
    const char *prefix = std::getenv("EQEMU_PACKET_TRACE");
    if (!prefix || !*prefix)
      return -1;
    std::string path =
        std::string(prefix) + "." + std::to_string(::getpid()) + ".bin";
    return ::open(path.c_str(), O_WRONLY | O_CREAT | O_APPEND | O_CLOEXEC,
                  0600);
  }();
  if (fd == -1)
    return;

  const char *raw_name = OpcodeManager::EmuToName(p->GetOpcode());
  std::string_view op = raw_name ? raw_name : "OP_Unknown";
  op = op.substr(0, std::min<size_t>(op.size(), 65535));
  peer = peer.substr(0, std::min<size_t>(peer.size(), 65535));

  // Frame body: microseconds UTC, direction stage, opcode name length,
  // peer name length, payload length, then the 3 variable-width pieces.
  const uint32_t body_length =
      static_cast<uint32_t>(18u + op.size() + peer.size() + p->size);
  std::vector<uint8_t> bytes;
  bytes.reserve(4u + body_length);
  const auto le = [&bytes](uint64_t value, unsigned n) {
    for (unsigned i = 0; i < n; ++i)
      bytes.push_back(static_cast<uint8_t>(value >> (8 * i)));
  };
  const auto us = std::chrono::duration_cast<std::chrono::microseconds>(
                      std::chrono::system_clock::now().time_since_epoch())
                      .count();
  le(body_length, 4);
  le(static_cast<uint64_t>(us), 8);
  le(server_to_client ? 0 : 1, 1); // 0 server->client, 1 client->server
  le(client_layout ? 1 : 0, 1);    // 0 EQEmu layout, 1 client layout
  le(op.size(), 2);
  le(peer.size(), 2);
  le(p->size, 4);
  bytes.insert(bytes.end(), op.begin(), op.end());
  bytes.insert(bytes.end(), peer.begin(), peer.end());
  if (p->size)
    bytes.insert(bytes.end(), p->pBuffer, p->pBuffer + p->size);

  // One append syscall per packet. A short write (e.g. full disk) is
  // deliberately not retried in the game-server hot path. Debug-only.
  (void)::write(fd, bytes.data(), bytes.size());
}
} // namespace PacketTrace
