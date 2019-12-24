from entities import Planet
from logic.output import CreatePlanetResponse
from logic.output import PlanetResponse 
from logic.exceptions import ParameterException

def create_planet(name, climate, terrain, datasource):
    planet_response = None
    if (datasource is None):
        raise ParameterException("DataSource is not acceptable")
    else:
        planet = Planet(name=name, climate=climate, terrain=terrain)
        planet = datasource.save(planet)
        planet_response = PlanetResponse(planet)
    return CreatePlanetResponse(planet = planet_response)