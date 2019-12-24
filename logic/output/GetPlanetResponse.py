from PlanetResponse import PlanetResponse

class GetPlanetResponse:
    def __init__(self, planets = None, page = 1):
        self.planets = planets
        self.page = page