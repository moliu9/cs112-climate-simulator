Design Check 10/21/2020: Climate Simulator

1)  What state will the simulator need to track?
    Be specific about the data structures you will use to track each piece of state.

    We need to keep track of the present year (updated as a float: self.year), the policies for each country, BAd amount for each country,
    (a dictionary), the global BAd amount (updated as a float: self.BAd_ppm), the countries and their temperatures
    (a list with a dictionary in the form of {'name': 'country name', 'temperature': 'country temperature'} for each
    country).

2)  Why does each policy’s emit method need to take in the same arguments?
    Think about the implementation of the simulator’s advance_year method.

    Because we call the same method on all policy classes. !

3)  What arguments should the emit methods take?

    emit(self, baseline: float, threshold: float, increment: float) emission data, and the temeparture 
