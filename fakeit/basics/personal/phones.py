from random import randint


def fake_local(area_code=None, body=None, mediator="-"):
    area_code = area_code or randint(100, 999)
    body = body or randint(1000000, 9999999)
    return f"{area_code}{mediator}{body}"


def fake_domestic(country_code=None, area_code=None, body=None, mediator="-"):
    country_code = country_code or randint(1, 99)
    area_code = area_code or randint(100, 999)
    body = body or randint(1000000, 9999999)
    return f"({country_code}) {area_code}{mediator}{body}"


def fake_dialed(country_code=None, area_code=None, body=None, mediator="-"):
    country_code = country_code or randint(1, 99)
    area_code = area_code or randint(100, 999)
    body = body or randint(1000000, 9999999)
    return f"{country_code}{mediator}{area_code}{mediator}{body}"


def fake_international(country_code=None, area_code=None, body=None, mediator="-"):
    country_code = country_code or randint(1, 99)
    area_code = area_code or randint(100, 999)
    body = body or randint(1000000, 9999999)
    return f"+{country_code}{mediator}{area_code}{mediator}{body}"
