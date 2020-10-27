class Simulator:
    """Simulates the climate of Branlex"""
    
    def __init__(self):
        self.year = 0
        self.max_temperature = 100
        self.country_names = []
        self.policies = {}
        self.BAd = 150  # initialize BAd level of 150ppm
        self.emission = {}  # initialize the emission data
        self.temperatures = {}  # initialize the temperature data
        
    def add_country(self, name: str, policy):
        """Adds a country and its policy to the simulation"""
        self.country_names.append(name)
        self.policies[name] = policy
        self.temperatures[name] = 0  # are these right?
        self.emission[name] = 0 # are these right?

    def find_neighbor_average(self, i, number_of_countries):
        """"Helper function that calculates the neighboring countries' average emission """
        average = 0
        if i == 0:  # the north-most country (has no northern neighbor)
            average = self.emission[self.country_names[i+1]]  # average equals to its southern neighbor's emission
        elif i == number_of_countries - 1:  # the south-most country (has no southern neighbor)
            average = self.emission[self.country_names[i-1]]  # average equals to its northern neighbor's emission
        else:  # countries in the middle
            average = (self.emission[self.country_names[i-1]] + self.emission[self.country_names[i+1]]) / 2
        return average

    def advance_year(self):
        """Advances the current year, updating country and global emissions and temperatures"""
        self.year += 1  # advance a year
        if self.BAd > 150:
            self.BAd -= 1  # reduce BAd by 1ppm (min 150 ppm)

        # calculate emission for each country using find_neighbor_average
        for i, country in enumerate(self.country_names):
            # store emission data in self.emission dictionary
            self.emission[country] = self.policies[country].emit(self.temperatures[country],
                                                                 self.find_neighbor_average(i, len(self.country_names)))
            # add every country's emission to the total global emission
            self.BAd += self.emission[country]

        # calculate temperature for the north-most country
        base_temp = (self.BAd / 5)
        # calculate the temperatures for the rest of the countries using temperature of north-most country
        for i, country in enumerate(self.country_names):
            self.temperatures[country] = base_temp + (i * 5)
        # halts entire process if temperature = max_temperature (stop)
            if self.temperatures[country] >= self.max_temperature:
                raise Exception("Temp has reached max for a country, we will all die. This is a catastrophe")

    def report(self):
        """Generates a report for use in the display"""
        return [{'name': country_name, 'temperature': country_temperature} for country_name, country_temperature
                in self.temperatures.items()]
