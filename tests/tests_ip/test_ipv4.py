from ipaddress import IPv4Address

from basics.ip.v4 import fake_ipv4


def test_ipv4():
    assert isinstance(fake_ipv4(), IPv4Address)
