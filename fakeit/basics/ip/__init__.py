import ipaddress

from fakeit.basics.numerics import fake_int


def fake_ipv4() -> ipaddress.IPv4Address:
    return ipaddress.IPv4Address(fake_int(0, 2 ** 32))


def fake_ipv6() -> ipaddress.IPv6Address:
    return ipaddress.IPv6Address(fake_int(0, 2 ** 128))
