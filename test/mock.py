from entities.planet import Planet


class Database:
    def __init__(self): 
        self.planets = []
        
        
    def save(self, p):
        x = Planet(id = -1, name = p.name, climate = p.climate, terrain = p.terrain, number_of_movies = 0)
        self.planets.append(x)
        return x


    def delete(self, id):
        x = filter(lambda x : True if x.id == id else False, self.planets)
        if x != []:
            self.planets.remove(x[0])
            return x[0]
        else:
            return None
    
    
    def get_all(self):
        return self.planets
    
    
    def get(self, id):
        return filter(lambda x : True if x.id == id else False, self.planets)
    
    
    def get_by_name(self, name):
        return filter(lambda x : True if x.name == name else False, self.planets)