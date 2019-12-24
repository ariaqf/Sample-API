from entities.planet import Planet
from logic.output.CreatePlanetResponse import CreatePlanetResponse


def create_planet(name, climate, terrain, queryable):
    p = None
    if (name != None and name != '' 
    and terrain != None and terrain != '' 
    and climate != None and climate != ''):
        pass
    else:
        p = Planet(name, climate, terrain)
        p = queryable.save(p)
    return CreatePlanetResponse(p)