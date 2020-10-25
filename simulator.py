from policies import *


class Simulator:
    """Simulates the climate of Branlex"""
    
    def __init__(self):
        self.year = 0
        self.max_temperature = 100
        self.country_names = []
        self.policies = {}
        # initialize BAd level of 150ppm
        self.BAd = 150
        # initialize the emission data
        self.emission = {}  # do we need this?
        self.temperatures = {}  # do we need this?
        self.report_data = []
        
    def add_country(self, name: str, policy):
        """Adds a country and its policy to the simulation"""
        self.country_names.append(name)
        self.policies[name] = policy
        
    def advance_year(self):
        """Advances the current year, updating country and global emissions and temperatures"""
        # advance a year
        self.year += 1
        # reduce BAd by 1ppm (min 150 ppm)
        if self.BAd > 150:
            self.BAd -= 1
        for country in self.country_names:
            # calculate emission for each country; store emission data in self.emission dictionary
            self.emission[country] = self.policies[country].emit(baseline, threshold, increment,
                                                                 self.temperatures, self.emission)
            self.BAd += self.emission[country]
        # calculate temperature for the north-most country
        base_temp = (self.BAd / 5)
        # calculate the temperatures for the rest of the countries
        for country in self.country_names:
            self.temperatures[country] = base_temp + (self.country_names.index(country) * 5)
        # halts entire process if temperature = max_temperature (stop)
            if self.temperatures[country] >= self.max_temperature:
                print("This is a catastrophic  event!")
                break  # is this right?

    def report(self):
        """Generates a report for use in the display"""
        # store data in the __init__ call on the list of hashtables
        return [{'name': country_name, 'temperature': country_temperature} for country_name, country_temperature
                in self.temperatures.items()]
