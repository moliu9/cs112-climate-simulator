class Simulator:
    """Simulates the climate of Branlex"""
    
    def __init__(self):
        self.year = 0
        self.max_temperature = 100
        self.country_names = []
        self.policies = {}
        # initialize BAd level of 150ppm
        self.BAd = 150
        
    def add_country(self, name: str, policy):
        """Adds a country and its policy to the simulation"""
        self.country_names.append(name)
        self.policies[name] = policy
        
    def advance_year(self):
        """Advances the current year, updating country and global emissions and temperatures"""

        # advance a year
        self.year += 1
        # reduce BAd by 1ppm (min 150 ppm)
        self.BAd -= 1
        # calculate emission for each country
        # store emission data in __init__
        # calculate global BAd amount
        total = sum(emission from all countries)
        # calculate temperature for each country
        # halts entire process if temperature = max_temperature (stop)

    def report(self):
        """Generates a report for use in the display"""
        # store data in the __init__ call on the list of hashtables
        return [{'name': 'Omelas', 'temperature': 20},
                {'name': 'Chalion', 'temperature': 85}]
