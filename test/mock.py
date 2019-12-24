from entities.planet import Planet
from logic import BaseSource
from math import ceil
from logic.data_output import PlanetsPage
 

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
        if records_per_page is None:
            records_per_page = len(self.planets)
        records_per_page = min(records_per_page,100)
        start_record = min((page-1)*records_per_page, len(self.planets))
        end_record = min((page)*records_per_page + 1, len(self.planets))
        total_pages = ceil(len(self.planets)/records_per_page)
        
        return PlanetsPage(self.planets[start_record:end_record],page,total_pages,records_per_page)
    
    
    def get(self, id):
        return list(filter(lambda x : True if x.id == id else False, self.planets))
    
    
    def get_by_name(self, name, page = 1, records_per_page = None):
        if records_per_page is None:
            records_per_page = len(self.planets)
        records_per_page = min(records_per_page,100)
        start_record = min((page-1)*records_per_page, len(self.planets))
        end_record = min((page)*records_per_page + 1, len(self.planets))
        total_pages = ceil(len(self.planets)/records_per_page)
        
        return PlanetsPage(list(filter(lambda x : True if x.name == name else False, self.planets))[start_record:end_record],page,total_pages,records_per_page)