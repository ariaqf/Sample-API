from entities.planet import Planet

class PlanetResponse:
    def __init__(self, planet = Planet()):
        self.id = planet.id
        self.name = planet.name
        self.climate = planet.climate
        self.terrain = planet.terrain
        self.number_of_movies = planet.number_of_movies
    

class PlanetPageResponse:
    def __init__(self, planets = None, page = 1, total_pages = 1, records_per_page = 100):
        self.planets = planets
        self.page = page
        self.total_pages = total_pages
        self.records_per_page = records_per_page