from base64 import b16encode, b32encode, b64encode
from os import urandom
from random import randint

from fakeit.exceptions import InvalidRange


def fake_bytes(min_length=0, max_length=16):
    if max_length < min_length:
        raise InvalidRange

    length = randint(min_length, max_length)
    return urandom(length)


def fake_b64(min_length=0, max_length=16):
    return b64encode(fake_bytes(min_length, max_length))


def fake_b32(min_length=0, max_length=16):
    return b32encode(fake_bytes(min_length, max_length))


def fake_b16(min_length=0, max_length=16):
    return b16encode(fake_bytes(min_length, max_length))
