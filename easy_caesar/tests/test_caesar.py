#!/usr/bin/env python3
#
from easy_caesar import Cipher


def test_encrypt():
    cipher = Cipher(1)
    assert cipher.encrypt("aaaa") == "bbbb"
