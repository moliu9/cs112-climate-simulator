class Baseline:
    """Emits at a constant rate"""
    def __init__(self, baseline: float):
        self.emission = baseline

    def emit(self, own_temperature, neighbor_average):
        return self.emission


class Reducing:
    """Reduces emissions every year"""
    def __init__(self, baseline: float, increment: float):
        self.emission = baseline
        self.increment = increment

    def emit(self, own_temperature, neighbor_average):
        if self.emission >= 0:
            self.emission -= self.increment
            if self.emission < 0:
                self.emission = 0
        return self.emission


class TemperaturePanic:
    """Emits at a constant rate until a temp threshold is reached"""
    def __init__(self, baseline: float, threshold: float, increment: float):
        self.emission = baseline
        self.threshold = threshold
        self.increment = increment

    def emit(self, own_temperature, neighbor_average):
        if own_temperature >= self.threshold:
            if self.emission > 0:
                self.emission -= self.increment
                if self.emission < 0:
                    self.emission = 0
        return self.emission


class NeighborAverage:
    """Adjusts emissions towards its neighbors' average"""
    def __init__(self, baseline: float, increment: float):
        self.emission = baseline
        self.increment = increment

    def emit(self, own_temperature, neighbor_average):
        if self.emission > neighbor_average:
            self.emission -= self.increment
            if self.emission < 0:
                self.emission = 0
        else:
            self.emission =+ self.increment
        return self.emission

