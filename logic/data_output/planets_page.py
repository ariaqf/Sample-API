class PlanetsPage:
    def __init__(self, planets, page, total_pages, records_per_page):
        self.planets = planets
        self.page = page
        self.total_pages = total_pages
        self.records_per_page = records_per_page