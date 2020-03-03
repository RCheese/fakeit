from random import choice

from constance.tld import domains, tlds

from ..personal.names import fake_name, fake_surname
from ..strings import fake_string


def fake_email(addr=None, domain=None, tld=None):
    addr = addr or f"{fake_string(min_length=1)}"
    domain = domain or f"{fake_string(min_length=1)}"
    tld = tld or f"{fake_string(min_length=2, max_length=7)}"
    return f"{addr}@{domain}.{tld}"


def fake_enough_email(addr=None, domain=None, tld=None):
    addr = addr or f"{fake_name()}.{fake_surname()}"
    domain = domain or f"{choice(domains)}"
    tld = tld or f"{choice(tlds)}"
    return f"{addr}@{domain}.{tld}"
