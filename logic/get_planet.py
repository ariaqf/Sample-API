from logic.output import PlanetPageResponse, PlanetResponse
from logic.exceptions import ParameterException

def get_planet(id, datasource):
    if(datasource is None):
        raise ParameterException("DataSource is not acceptable")
    
    ret = datasource.get(id)
    return PlanetPageResponse(
        list(map(lambda x: PlanetResponse(x), ret.planets)),
        page = ret.page,
        total_pages = ret.total_pages,
        records_per_page = ret.records_per_page
    )