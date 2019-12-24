import pytest
from logic import search_planet
from test.mock import Database
from entities import Planet
from logic.exceptions import ParameterException

queryable = Database()

def test_search_no_queryable():
    try:
        ret = search_planet('Test', None)
    except ParameterException as e:
        assert e.__str__() == 'DataSource is not acceptable'
    

def test_search_no_planet():
    ret = search_planet('Test', queryable)
    assert ret.page == 1
    assert ret.pages == 0
    assert len(ret.planets) == 0