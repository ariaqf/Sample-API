from logic.output import PlanetPageResponse, PlanetResponse
from logic.exceptions import ParameterException

def search_planet(name, queryable, page = 1, records_per_page = 10):
    if(queryable is None):
        raise ParameterException("DataSource is not acceptable")
    ret = queryable.get_by_name(name, records_per_page = records_per_page, page = page)
    return ret #list(map(lambda x: PlanetResponse(x), ret))
    