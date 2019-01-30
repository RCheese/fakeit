from os import urandom
from random import randint
from fakeit.exceptions import InvalidRange
from base64 import b64encode


def fake_bytes(min_length=0, max_length=16):
    if max_length < min_length:
        raise InvalidRange

    length = randint(min_length, max_length)
    return urandom(length)


def fake_b64(min_length=0, max_length=16):
    return b64encode(fake_bytes(min_length, max_length))
