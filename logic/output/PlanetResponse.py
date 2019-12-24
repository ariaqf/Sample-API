from entities.planet import Planet

class PlanetResponse:
    def __init__(self, planet = Planet()):
        self.id = planet.id
        self.name = planet.name
        self.climate = planet.climate
        self.terrain = planet.terrain
        self.number_of_movies = planet.number_of_movies
    