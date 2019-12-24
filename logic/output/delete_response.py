from logic.output.planet_response import PlanetResponse

class DeletePlanetResponse:
    def __init__(self, planet = None):
        self.planet = PlanetResponse(planet)