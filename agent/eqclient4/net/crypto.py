"""Login DES-CBC. Key and IV are eight zero bytes, matching eqcrypt_block."""

from __future__ import annotations

from typing import Protocol

from Crypto.Cipher import DES


class _Block(Protocol):
    def encrypt(self, data: bytes) -> bytes: ...

    def decrypt(self, data: bytes) -> bytes: ...


def _cipher() -> _Block:
    return DES.new(b"\x00" * 8, DES.MODE_CBC, iv=b"\x00" * 8)


def zero_pad(data: bytes) -> bytes:
    if len(data) % 8:
        data += b"\x00" * (8 - (len(data) % 8))
    return data


def encrypt_block(plain: bytes) -> bytes:
    return _cipher().encrypt(zero_pad(plain))


def decrypt_block(cipher: bytes) -> bytes:
    if not cipher or len(cipher) % 8:
        raise ValueError("DES ciphertext length must be a multiple of 8")
    return _cipher().decrypt(cipher)
