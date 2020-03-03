from uuid import uuid1, uuid3, uuid4, uuid5


def fake_uuid1(node=None, clock_seq=None):
    return uuid1(node, clock_seq)


def fake_uuid3(namespace, name):
    return uuid3(namespace, name)


def fake_uuid4():
    return uuid4()


def fake_uuid5(namespace, name):
    return uuid5(namespace, name)


def fake_uuid():
    return fake_uuid4()
