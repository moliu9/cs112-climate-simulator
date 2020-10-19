class Baseline:
    """Emits at a constant rate"""
    def __init__(self, baseline: float):
        pass

    def emit(self):
        pass
    
class Reducing:
    """Reduces emissions every year"""
    def __init__(self, baseline: float, increment: float):
        pass

    def emit(self):
        pass

class TemperaturePanic:
    """Emits at a constant rate until a temp threshold is reached"""
    def __init__(self, baseline: float, threshold: float, increment: float):
        pass

    def emit(self):
        pass

class NeighborAverage:
    """Adjusts emissions towards its neighbors' average"""
    def __init__(self, baseline: float, increment: float):
        pass

    def emit(self):
        pass