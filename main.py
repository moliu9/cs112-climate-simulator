from display import Display
from simulator import Simulator
import policies

if __name__ == '__main__':
    sim = Simulator()
    sim.add_country('Atlantis', policies.Baseline(0.1))
    sim.add_country('Omelas', policies.Reducing(5, 0.1))
    sim.add_country('Vulcan', policies.NeighborAverage(2, 1))
    sim.add_country('Arcadia', policies.TemperaturePanic(2, 60, 1))
    sim.add_country('Chalion', policies.Reducing(2, 0.1))
    display = Display(sim)
    display.run()
