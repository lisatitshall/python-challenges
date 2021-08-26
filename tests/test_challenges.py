import pytest
from programs.challenges import func_1_methods, func_1_no_methods, func_2

def test_func_1_methods():
    assert func_1_methods("Hello world") == "hello world"
    assert func_1_methods("Hello World!") == "HELLO WORLD!"

def test_func_1_no_methods():
    assert func_1_no_methods("Hello world") == "hello world"
    assert func_1_no_methods("Hello World!") == "HELLO WORLD!"

def test_func_2():
    assert func_2("Home", ["hole", "dome", "dove", "hail"]) == ["hole", "dome"]
    assert func_2("wall", ["Wail", "warm", "tall", "worn"]) == ["Wail", "tall"]