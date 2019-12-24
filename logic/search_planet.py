from logic.output import GetPlanetResponse, PlanetResponse
from logic.exceptions import ParameterException

def search_planet(name, queryable):
    if(queryable is None):
        raise ParameterException("DataSource is not acceptable")
    ret = queryable.get_by_name(name)
    return list(map(lambda x: PlanetResponse(x), ret))
    