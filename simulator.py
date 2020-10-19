class Simulator:
    """Simulates the climate of Branlex"""
    
    def __init__(self):
        self.year = 0
        self.max_temperature = 100
        self.country_names = []
        self.policies = {}
        # initialize BAd level - how to do this?
        self.BAd_ppm = 150
        
    def add_country(self, name: str, policy):
        """Adds a country and its policy to the simulation"""
        self.country_names.append(name)
        self.policies[name] = policy
        
    def advance_year(self):
        """Advances the current year, updating country and global emissions and temperatures"""

        # only implement if temp < max temp
        if temperature > max_temperature for any country in self.policies:
            print('This is a catastrophe!')
        else:
            # advance a year
            self.year += 1
            # reduce BAd by 1ppm (min 150 ppm)
            self.BAd_ppm -= 1
            # calculate emission for each country
            # calculate total BAd emission
            total = sum(emission from all countries)
            # calculate temperature for each country

    def report(self):
        """Generates a report for use in the display"""
        return [{'name': 'Omelas', 'temperature': 20},
                {'name': 'Chalion', 'temperature': 85}]
