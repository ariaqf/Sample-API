from logic.output import DeletePlanetResponse
from logic.output import PlanetResponse
from logic.exceptions import ParameterException

def delete_planet(id, queryable):
    delete_response = None
    if(queryable is None):
        raise ParameterException("DataSource is not acceptable")
    ret = queryable.delete(id)
    if ret is not None:
        delete_response = DeletePlanetResponse(PlanetResponse(ret))

    return delete_response