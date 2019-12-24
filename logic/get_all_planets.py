from logic.output import GetPlanetResponse, PlanetResponse
from logic.exceptions import ParameterException

def get_all(queryable):
    if(queryable is None):
        raise ParameterException("DataSource is not acceptable")
    ret = queryable.get_all()
    return list(map(lambda x: PlanetResponse(x), ret))
    