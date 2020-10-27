from simulator import Simulator
import policies


# testing find_neighbor_average helper function
def test_find_neighbor_average():
    s = Simulator()
    s.country_names = ['Atlantis', 'Omelas', 'Vulcan', 'Arcadia', 'Chalion']
    s.emission = {'Atlantis': 10, 'Omelas': 16, 'Vulcan': 18, 'Arcadia': 22, 'Chalion': 47}
    # the north most country refers to its southern neighbor
    assert s.find_neighbor_average(0, 5) == 16
    # the south most country refers to its northern neighbor
    assert s.find_neighbor_average(4, 5) == 22
    # the middle country should have the average of its neighbors
    assert s.find_neighbor_average(2, 5) == 19


# testing functionalities inside the advance_year method
# testing advancing a year in time
def test_year():
    s = Simulator()
    # year is zero initially
    assert s.year == 0
    # year advancing by one
    s.advance_year()
    assert s.year == 1


# testing controlling the natural decrease of BAd
def test_BAd_level():
    s = Simulator()
    s.advance_year()
    # BAd should be 150ppm initially
    assert s.BAd == 150
    # if BAd is below 150, do nothing
    s.BAd = 130
    s.advance_year()
    assert s.BAd == 130
    # if BAd is above 150, decrease by 1 ppm
    s.BAd = 160
    s.advance_year()
    assert s.BAd == 159


# testing that the country emissions are updated correctly
def test_country_emissions():
    s = Simulator()
    s.add_country('Atlantis', policies.Baseline(1))
    s.add_country('Omelas', policies.Baseline(1))
    s.add_country('Vulcan', policies.Baseline(1))
    s.add_country('Arcadia', policies.Baseline(1))
    s.add_country('Chalion', policies.Baseline(1))
    # check that initial emissions are zero
    assert s.emission == {'Atlantis': 0, 'Omelas': 0, 'Vulcan': 0, 'Arcadia': 0, 'Chalion': 0}
    # check that the new emissions are updated
    s.advance_year()
    assert s.emission == {'Atlantis': 1, 'Omelas': 1, 'Vulcan': 1, 'Arcadia': 1, 'Chalion': 1}


# check that global BAd is updated using country emissions
def test_global_BAd():
    s = Simulator()
    s.add_country('Atlantis', policies.Baseline(1))
    s.add_country('Omelas', policies.Baseline(1))
    s.add_country('Vulcan', policies.Baseline(1))
    s.add_country('Arcadia', policies.Baseline(1))
    s.add_country('Chalion', policies.Baseline(1))
    # check that the initial BAd level if 150 ppm
    assert s.BAd == 150
    # check that the global emission is increased by the sum of countries' emissions
    s.advance_year()
    assert s.BAd == 150 + 5


# testing that country temperatures are updated
def test_country_temperatures():
    # update while temperature does not exceed max temperature
    # exception raised when
    # with pytest.raises(Exception):
    pass


# testing that the report is displayed in desired manner
def test_report():
    pass




