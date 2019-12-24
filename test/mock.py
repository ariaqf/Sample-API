from entities.planet import Planet
from logic import BaseSource
 

class Database(BaseSource):
    def __init__(self): 
        self.planets = []
        
        
    def save(self, p):
        x = Planet(id = p.id, name = p.name, climate = p.climate, terrain = p.terrain)
        self.planets.append(x)
        return x


    def delete(self, id):
        x = list(filter(lambda x : True if x.id == id else False, self.planets))
        if x != []:
            self.planets.remove(x[0])
            return x[0]
        else:
            return None
    
    
    def get_all(self, page = 1, records_per_page = None):
        start_record = min((page-1)*records_per_page, len(self.planets))
        end_record = min((page)*records_per_page + 1, len(self.planets))
        return self.planets[start_record:end_record]
    
    
    def get(self, id):
        return list(filter(lambda x : True if x.id == id else False, self.planets))
    
    
    def get_by_name(self, name, page = 1, records_per_page = None):
        start_record = min((page-1)*records_per_page, len(self.planets))
        end_record = min((page)*records_per_page + 1, len(self.planets))
        return list(filter(lambda x : True if x.name == name else False, self.planets))[start_record:end_record]