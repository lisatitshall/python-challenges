import pytest
from programs.challenges import func_1, func_2

def test_func_1():
    assert func_1("Hello world") == "hello world"
    assert func_1("Hello World!") == "HELLO WORLD!"

def test_func_2():
    assert func_2("Home", ["hole", "dome", "dove", "hail"]) == ["hole", "dome"]
    assert func_2("wall", ["Wail", "warm", "tall", "worn"]) == ["Wail", "tall"]