import pytest
from logic import create_planet
from test.mock import Database
from logic.exceptions import ParameterException

queryable = Database()

def test_create_no_queryable():
    try:
        create_planet('None', 'None', 'None', None)
        assert 1 == 0 # This line should never be reached except if the logic changes
    except ParameterException as e:
        assert e.__str__() == 'DataSource is not acceptable'


def test_create_no_data():
    ret = create_planet(None, None, None, queryable)
    assert ret.planet is not None


def test_create_partial_data():
    ret = create_planet('A', 'B', None, queryable)
    assert ret.planet is not None

    ret = create_planet('A', None, 'C', queryable)
    assert ret.planet is not None
    
    ret = create_planet(None, 'B', 'C', queryable)
    assert ret.planet is not None

    
def test_create_test():
    ret = create_planet('A', 'B', 'C', queryable)
    assert ret.planet is not None
