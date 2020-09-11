from ipaddress import IPv6Address

from fakeit.basics.ip.v6 import fake_ipv6


def test_ipv4():
    assert isinstance(fake_ipv6(), IPv6Address)
