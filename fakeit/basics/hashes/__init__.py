from hashlib import md5, sha1, sha256
from ..bytes import fake_bytes


def fake_md5():
    return md5(fake_bytes()).hexdigest()


def fake_sha1():
    return sha1(fake_bytes()).hexdigest()


def fake_sha256():
    return sha256(fake_bytes()).hexdigest()
