from logic.output.PlanetResponse import PlanetResponse

class DeletePlanetResponse:
    def __init__(self, planet = None):
        self.planet = PlanetResponse(planet)