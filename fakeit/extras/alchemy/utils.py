from copy import deepcopy
from functools import wraps

from fakeit.basics.boolean import fake_bool
from fakeit.basics.numerics import fake_float, fake_int
from fakeit.basics.strings import fake_string
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql.schema import Table


def _tableconvert(func):
    @wraps(func)
    def wrapped(cls_or_rbl, *args, **kwargs):
        if isinstance(cls_or_rbl, Table):
            table = cls_or_rbl
        elif isinstance(cls_or_rbl, DeclarativeMeta):
            table = cls_or_rbl.__table__
        else:
            raise TypeError
        return func(table, *args, **kwargs)

    return wrapped


@_tableconvert
def get_not_nullable(table):
    return (x for x in table.c if not x.nullable)


def python_type_cast(column):
    return column.type.python_type


@_tableconvert
def get_template(table):
    return dict((column.name, column.type) for column in table.c)


@_tableconvert
def get_basic_template(table):
    return dict((column.name, column.type) for column in table.c if not column.nullable)


type_mapping = {str: fake_string, int: fake_int, float: fake_float, bool: fake_bool}


def fill_template(template, id=None, **kwargs):
    tmpl = deepcopy(template)
    res = {}
    if "id" in tmpl:
        tmpl.pop("id")
        if id is None:
            id = fake_int(0, 128)

    for k, v in tmpl.items():
        if k in kwargs:
            res[k] = kwargs[k]() if callable(kwargs[k]) else kwargs[k]
        elif v.python_type == int:
            res[k] = type_mapping[int](0, 777)
        elif v.python_type == float:
            res[k] = type_mapping[float](0, 777)
        elif v.python_type == str:
            res[k] = type_mapping[str](max_length=v.length)
        elif v.python_type == bool:
            res[k] = type_mapping[bool]()
        else:
            res[k] = None

    if ("id" in template) or id:
        res["id"] = id
    return res
