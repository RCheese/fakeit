from ipaddress import IPV4LENGTH, IPv4Address
from random import choice

from basics.numerics import fake_int


def fake_ipv4() -> IPv4Address:
    "<0.0.0.0/0> | <0.0.0.0; 255.255.255.255>"
    return IPv4Address(fake_int(0, 2 ** IPV4LENGTH - 1))


def fake_ipv4_24() -> IPv4Address:
    "<10.0.0.0/8> | <10.0.0.0; 10.255.255.255>"
    return IPv4Address(fake_int(10 * 2 ** 24, 11 * 2 ** 24 - 1))


def fake_ipv4_20() -> IPv4Address:
    "<172.16.0.0/12> | <172.16.0.0; 172.31.255.255>"
    return IPv4Address(fake_int(2886729728, 2887778303))


def fake_ipv4_16() -> IPv4Address:
    "<192.168.0.0/16> | <192.168.0.0; 192.168.255.255>"
    return IPv4Address(fake_int(3232235520, 3232301055))


def fake_ipv4_local() -> IPv4Address:
    """
    On of
    <192.168.0.0/16> | <192.168.0.0; 192.168.255.255>
    <172.16.0.0/12> | <172.16.0.0; 172.31.255.255>
    <10.0.0.0/8> | <10.0.0.0; 10.255.255.255>
    """
    return choice((fake_ipv4_16(), fake_ipv4_20(), fake_ipv4_24()))


def fake_ipv4_broadcast() -> IPv4Address:
    "<255.255.255.255/32> | <255.255.255.255; 255.255.255.255>"
    return IPv4Address(2 ** 32 - 1)


def fake_ipv4_multicast() -> IPv4Address:
    "<224.0.0.0/4> | <224.0.0.0; 239.255.255.255>"
    return IPv4Address(fake_int(3758096384, 4026531839))


def fake_ipv4_class_d() -> IPv4Address:
    "<224.0.0.0/4> | <224.0.0.0; 239.255.255.255>"
    return fake_ipv4_multicast()


def fake_ipv4_class_e() -> IPv4Address:
    "<240.0.0.0/4> | <240.0.0.0; 255.255.255.254>"
    return IPv4Address(fake_int(4026531840, 4294967294))


def fake_ipv4_test_net_1() -> IPv4Address:
    "<192.0.2.0/24> | <192.0.2.0; 192.0.2.255>"
    return IPv4Address(fake_int(3221225984, 3221226239))


def fake_ipv4_test_net_2() -> IPv4Address:
    "<198.51.100.0/24> | <198.51.100.0; 198.51.100.255>"
    return IPv4Address(fake_int(3325256704, 3325256959))


def fake_ipv4_test_net_3() -> IPv4Address:
    "<203.0.113.0/24> | <203.0.113.0; 203.0.113.255>"
    return IPv4Address(fake_int(3405803776, 3405804031))


def fake_ipv4_inter_network() -> IPv4Address:
    "<198.18.0.0/15> | <198.18.0.0; 198.19.255.255>"
    return IPv4Address(fake_int(3323068416, 3323199487))


def fake_ipv4_ipv6_relay() -> IPv4Address:
    "<192.88.99.0/24> | <192.88.99.0; 192.88.99.255>"
    return IPv4Address(fake_int(3227017984, 3227018239))


def fake_ipv4_ietf_private() -> IPv4Address:
    "<192.0.0.0/24> | <192.0.0.0; 192.0.0.255>"
    return IPv4Address(fake_int(3221225472, 3221225727))


def fake_ipv4_subnet() -> IPv4Address:
    "<169.254.0.0/16> | <169.254.0.0; 169.254.255.255>"
    return IPv4Address(fake_int(2851995648, 2852061183))


def fake_ipv4_loopback() -> IPv4Address:
    "<127.0.0.0/8> | <127.0.0.0; 127.255.255.255>"
    return IPv4Address(fake_int(2130706432, 2147483647))


def fake_ipv4_shared_address() -> IPv4Address:
    "<100.64.0.0/10> | <100.64.0.0; 100.127.255.255>"
    return IPv4Address(fake_int(1681915904, 1686110207))


def fake_ipv4_current() -> IPv4Address:
    "<0.0.0.0/8> | <0.0.0.0; 0.255.255.255>"
    return IPv4Address(fake_int(0, 16777215))
