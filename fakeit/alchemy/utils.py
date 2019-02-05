from copy import deepcopy

from fakeit.basics.numerics import fake_int, fake_float
from fakeit.basics.strings import fake_string


def get_not_nullable(table):
    return (x for x in table.c if not x.nullable)


def python_type_cast(column):
    return column.type.python_type


def get_template(table):
    return dict((column.name, column.type) for column in table.c)


def get_basic_template(table):
    return dict((column.name, column.type) for column in table.c if not column.nullable)


type_mapping = {
    str: fake_string,
    int: fake_int,
    float: fake_float
}


def fill_template(template, id=None):
    tmpl = deepcopy(template)
    res = {}
    if "id" in tmpl:
        tmpl.pop("id")
        if id is None:
            id = fake_int(0, 128)

    for k, v in tmpl.items():
        if v.python_type == int:
            res[k] = type_mapping[int](0, 777)
        elif v.python_type == float:
            res[k] = type_mapping[float](0, 777)
        elif v.python_type == str:
            res[k] = type_mapping[str](max_length=v.length)
        else:
            res[k] = None

    if ("id" in template) or id:
        res["id"] = id
    return res
