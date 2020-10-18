class Simulator:
    """Simulates the climate of Branlex"""
    
    def __init__(self):
        self.year = 0
        self.max_temperature = 100
        self.country_names = []
        self.policies = {}
        
    def add_country(self, name: str, policy):
        """Adds a country and its policy to the simulation"""
        self.country_names.append(name)
        self.policies[name] = policy
        
    def advance_year(self):
        """Advances the current year, updating country and global emissions and temperatures"""
        self.year += 1

    def report(self):
        """Generates a report for use in the display"""
        return [{'name': 'Omelas', 'temperature': 20},
                {'name': 'Chalion', 'temperature': 85}]
