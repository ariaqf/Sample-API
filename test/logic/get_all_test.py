import pytest
from logic import get_all
from test.mock import Database
from entities import Planet
from logic.exceptions import ParameterException

queryable = Database()

def test_get_all_no_queryable():
    try:
        get_all(None)
        assert 1 == 0 # This line should never be reached except if the logic changes
    except ParameterException as e:
        assert e.__str__() == 'DataSource is not acceptable'
        
def test_get_all_empty():
    ret = get_all(queryable)
    assert ret.planets == []
    assert ret.page == 1
    assert ret.total_pages == 1
    
def test_get_all():
    for x in range(4):
        i = x+1
        queryable.save(Planet(id = i, 
                              name = "Planet{}".format(i),
                              climate = "Climate{}".format(i),
                              terrain = "Terrain{}".format(i),
                              number_of_movies= -1))
    ret = get_all(queryable)
    assert len(ret.planets) == 4
    assert ret.page == 1
    assert ret.total_pages == 1
    queryable.clean()
 
def test_get_all_page():
    for x in range(4):
        i = x+1
        queryable.save(Planet(id = i, 
                              name = "Planet{}".format(i),
                              climate = "Climate{}".format(i),
                              terrain = "Terrain{}".format(i),
                              number_of_movies= -1))
    ret = get_all(queryable, records_per_page=2)
    assert len(ret.planets) == 2
    assert ret.page == 1
    assert ret.total_pages == 2
    queryable.clean()