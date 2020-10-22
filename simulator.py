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
        self.temperatures = []  # do we need this?#
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
        fst_country_temp = (self.BAd_ppm / 5)
        for country in self.country_names:
            # calculate emission for each country
            # store emission data in __init__
            # calculate temperature for each country
            new_temp = fst_country_temp + (self.country_names.index(country) * 5)
            self.temperatures.append(new_temp)
            self.emission[country] = country.emit(baseline, threshold, increment, self.temperatures, self.emission)
            self.BAd += self.emission[country]
            # halts entire process if temperature = max_temperature (stop)
            # base temp
            if new_temp >= self.max_temperature:
                print("This is a catastrophic  event!")
            else:
                report_data.append[{'name': country, 'temperature': new_temp}]
        return report_data

    def report(self):
        """Generates a report for use in the display"""
        # store data in the __init__ call on the list of hashtables
        return self.report_data
