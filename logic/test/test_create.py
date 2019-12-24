import pytest
from logic.create_planet import create_planet
from logic.test.mock import Database

queryable = Database()

def create_no_queryable():
    ret = create_planet(None, None, None, None)
    assert ret.planet == None


def create_no_data():
    ret = create_planet(None, None, None, queryable)
    assert ret.planet == None


def create_partial_data():
    ret = create_planet('A', None, None, queryable)
    assert ret.planet == None
    
    ret = create_planet('A', 'B', None, queryable)
    assert ret.planet == None

    ret = create_planet('A', None, 'C', queryable)
    assert ret.planet == None
    
    ret = create_planet(None, 'B', 'C', queryable)
    assert ret.planet == None

    
def create_test():
    ret = create_planet('A', 'B', 'C', queryable)
    assert ret.planet != None
