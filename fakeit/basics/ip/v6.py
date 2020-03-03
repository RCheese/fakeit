from ipaddress import IPV6LENGTH, IPv6Address

from basics.numerics import fake_int


def fake_ipv6() -> IPv6Address:
    return IPv6Address(fake_int(0, 2 ** IPV6LENGTH))
