import pytest
from logic import create_planet, get_planet
from test.mock import Database
from entities import Planet
from logic.exceptions import ParameterException

queryable = Database()

def test_get_no_queryable():
    try:
        ret = get_planet('Test', None)
    except ParameterException as e:
        assert e.__str__() == 'DataSource is not acceptable'
    

def test_get_no_planet(): 
    ret = get_planet('Test', queryable) 
    assert ret.planets == []
    assert ret.page == 1
    assert ret.total_pages == 1
    
def test_number_of_movies():
    created = create_planet('Tatooine', 'A', 'B', queryable)
    ret = get_planet(created.planet.id, queryable)
    assert ret.planets[0].number_of_movies > 0