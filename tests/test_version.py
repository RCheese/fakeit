import pytest

import toml

from fakeit import __verison__


def test_version():
    with open("pyproject.toml") as f:
        tf = toml.load(f)
        print(tf)
        assert tf["tool"]["poetry"]["version"] == __verison__
