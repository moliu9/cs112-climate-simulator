class Baseline:
    """Emits at a constant rate"""
    def __init__(self, baseline: float):
        self.baseline = baseline

    def emit(self, baseline: float, threshold: float, increment: float, emission: dict, temperature : dict):
        emission[self] += baseline


class Reducing:
    """Reduces emissions every year"""
    def __init__(self, baseline: float, increment: float):
        self.baseline = baseline
        self.increment = increment

    def emit(self, baseline: float, threshold: float, increment: float, emission: dict, temperature : dict):
        if emission[self] > 0:
            emission[self] += (baseline - increment)


class TemperaturePanic:
    """Emits at a constant rate until a temp threshold is reached"""
    def __init__(self, baseline: float, threshold: float, increment: float):
        self.baseline = baseline
        self.threshold = threshold
        self.increment = increment

    def emit(self, baseline: float, threshold: float, increment: float, emission: dict, temperature: dict):
        if temperature >= threshold:
            if emission[self] > 0:
                emission[self] += (baseline - increment)
        else:
            emission[self] += baseline


class NeighborAverage:
    """Adjusts emissions towards its neighbors' average"""
    def __init__(self, baseline: float, increment: float):
        self.baseline = baseline
        self.increment = increment

    def emit(self, baseline: float, threshold: float, increment: float, temperature: list, emission: dict):
        avg_temp = (sum(temperature) / len(temperature))
        if avg_temp <= emission[self]:
            emission[self] += (baseline - increment)
        else:
            emission[self] += baseline