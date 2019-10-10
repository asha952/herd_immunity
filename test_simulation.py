from simulation import Simulation
from virus import Virus
from person import Person

def test_constructor():
    virus = Virus("HIV", 0.24, 0.12)
    sim = Simulation(10, .4, virus, 2)

    assert sim.pop_size == 10
    assert sim.virus == virus
    assert sim.initial_infected == 2
    assert sim.vacc_percentage == .4


def test_simulation_should_continue():
    virus = Virus("HIV", 0.24, 0.12)
    sim = Simulation(10, .4, virus, 2)

    assert sim._simulation_should_continue()

def test_interactor():
    
