from ipaddress import IPV4LENGTH, IPv4Address
from random import choice

from basics.numerics import fake_int


def fake_ipv4() -> IPv4Address:
    return IPv4Address(fake_int(0, 2 ** IPV4LENGTH))


def fake_ipv4_24() -> IPv4Address:
    return IPv4Address(fake_int(10 * 2 ** 24, 11 * 2 ** 24))


def fake_ipv4_20() -> IPv4Address:
    return IPv4Address(fake_int(2886729728, 2887778304))


def fake_ipv4_16() -> IPv4Address:
    return IPv4Address(fake_int(3232235520, 3232301056))


def fake_ipv4_local() -> IPv4Address:
    return choice((fake_ipv4_16(), fake_ipv4_20(), fake_ipv4_24()))


def fake_ipv4_broadcast_netwok() -> IPv4Address:
    return IPv4Address(2 ** 32 - 1)


def fake_ipv4_broadcast() -> IPv4Address:
    return IPv4Address(fake_int(3221225984, 3221226240))


def fake_ipv4_multicast() -> IPv4Address:
    return IPv4Address(fake_int(3758096384, 4026531840))
