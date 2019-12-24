from logic.output.PlanetResponse import PlanetResponse

class CreatePlanetResponse:
    def __init__(self, planet = None, status = 0):
        self.planet = PlanetResponse(planet)