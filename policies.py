class Baseline:
    """Emits at a constant rate"""
    def __init__(self, baseline: float):
        self.emission = baseline  # set baseline as the initial emission property

    def emit(self, own_temperature, neighbor_average):
        return self.emission  # emit the same amount


class Reducing:
    """Reduces emissions every year"""
    def __init__(self, baseline: float, increment: float):
        self.emission = baseline
        self.increment = increment

    def emit(self, own_temperature, neighbor_average):
        if self.emission >= 0:  # if the emission is equal to or greater than zero
            self.emission -= self.increment  # decrease by set increment
            if self.emission < 0:  # if the emission goes below zero
                self.emission = 0
        return self.emission


class TemperaturePanic:
    """Emits at a constant rate until a temp threshold is reached"""
    def __init__(self, baseline: float, threshold: float, increment: float):
        self.emission = baseline
        self.threshold = threshold
        self.increment = increment

    def emit(self, own_temperature, neighbor_average):
        if own_temperature >= self.threshold:  # if the temperature is higher than threshold
            if self.emission > 0:  # and the emission is more than zero
                self.emission -= self.increment  # decrease emission by increment
                if self.emission < 0:  # if the emission goes below zero
                    self.emission = 0
        return self.emission


class NeighborAverage:
    """Adjusts emissions towards its neighbors' average"""
    def __init__(self, baseline: float, increment: float):
        self.emission = baseline
        self.increment = increment

    def emit(self, own_temperature, neighbor_average):
        if self.emission > neighbor_average:  # if the emission is higher than neighbors' average
            self.emission -= self.increment  # decrease emission by increment
            if self.emission < 0:  # if the emission goes below zero
                self.emission = 0
        else:
            self.emission += self.increment  # if the emission is lower than or equal to neighbors' average
        return self.emission

