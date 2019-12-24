from logic.output.PlanetResponse import PlanetResponse

class CreatePlanetResponse:
    def CreatePlanetResponse(self, planet = None, status = 0):
        self.planet = PlanetResponse(planet)