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
