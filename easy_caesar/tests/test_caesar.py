#!/usr/bin/env python3
#
import pytest
from easy_caesar import Cipher


@pytest.mark.parametrize(
    "value, step, expected",
    [("aaaa", 1, "bbbb"), ("cc", 3, "ff"), ("abcde", 5, "fghij")],
)
def test_encrypt(value, step, expected):
    cipher = Cipher(step)
    assert cipher.encrypt(value) == expected
