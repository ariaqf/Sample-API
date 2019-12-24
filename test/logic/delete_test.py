import pytest
from entities import Planet
from logic import delete_planet
from logic.exceptions import ParameterException
from test.mock import Database
 
queryable = Database()

def test_delete_no_id():
    ret = delete_planet(None, queryable)
    assert ret is None
    
def test_delete_no_queryable():
    try:
        ret = delete_planet(id, None)
    except ParameterException as e:
        assert e.__str__() == 'DataSource is not acceptable'

def test_existing_delete():
    id = 1
    queryable.save(Planet(id = 1, name = 'test', climate = 'test', terrain = 'test', number_of_movies=10))
    ret = delete_planet(id,queryable)
    assert ret.planet.id == id
    
def test_non_existing_delete():
    id = 1
    ret = delete_planet(id,queryable)
    assert ret is None