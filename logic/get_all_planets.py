from logic.output import PlanetPageResponse, PlanetResponse
from logic.exceptions import ParameterException

def get_all(queryable, page = 1, records_per_page = None):
    if(queryable is None):
        raise ParameterException("DataSource is not acceptable")
    ret = queryable.get_all(page, records_per_page)
    
    return PlanetPageResponse(
        list(map(lambda x: PlanetResponse(x), ret.planets)),
        page = ret.page,
        total_pages = ret.total_pages,
        records_per_page = ret.records_per_page
    )
     