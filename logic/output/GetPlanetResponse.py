from logic.output.PlanetResponse import PlanetResponse

class GetPlanetResponse:
    def __init__(self, planets = None, page = 1, total_pages = 1, records_per_page = 100):
        self.planets = planets
        self.page = page
        self.total_pages = total_pages
        self.records_per_page = records_per_page