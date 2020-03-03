import pytest
from logic import search_planet, create_planet
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
    assert ret.total_pages == 1
    assert len(ret.planets) == 0

def test_search_created():
    created = create_planet('A', 'B', 'C', queryable).planet
    ret = search_planet(created.name, queryable)
    assert ret.page == 1 
    assert ret.total_pages == 1
    assert len(ret.planets) == 1
    assert ret.planets[0].name == created.name        
    queryable.clean()
    
def test_search_pages():
    created1 = create_planet('A', 'B', 'C', queryable).planet
    created2 = create_planet('ABC', 'B', 'C', queryable).planet
    created3 = create_planet('BACA', 'B', 'C', queryable).planet
    created4 = create_planet('PPP', 'B', 'C', queryable).planet
    ret = search_planet(created1.name, queryable, records_per_page = 2)
    assert ret.page == 1 
    assert ret.total_pages == 2
    assert len(ret.planets) == 2
    assert ret.planets[0].name.count('A') > 0 
    assert ret.planets[1].name.count('A') > 0
    queryable.clean()

def test_search_partial():
    created1 = create_planet('A', 'B', 'C', queryable).planet
    created2 = create_planet('ABC', 'B', 'C', queryable).planet
    created3 = create_planet('BACA', 'B', 'C', queryable).planet
    created4 = create_planet('PPP', 'B', 'C', queryable).planet
    ret = search_planet(created1.name, queryable)
    assert ret.page == 1 
    assert ret.total_pages == 1
    assert len(ret.planets) == 3
    assert ret.planets[0].name.count('A') > 0
    assert ret.planets[1].name.count('A') > 0
    assert ret.planets[2].name.count('A') > 0
    queryable.clean()