from simulator import *
import pytest


# testing find_neighbor_average helper function
def test_find_neighbor_average():
    # the north most country
    # the south most country
    # the middle countries


# testing advance_year method
s = Simulator()

# testing that we advance a year in time
def test_year():
    assert s.year == 0
    s.advance_year()
    assert s.year == 1


# testing that we are controlling the natural decrease of BAd
def test_BAd_level():
    # if BAd is below 150, do nothing
    # if BAd is above 150, decrease by 1 ppm


# testing that the country emissions are updated
def test_country_emissions():
    # if the BAd
    assert s.emission['country'] ==


# testing that global BAd is updated using country emissions
def test_global_BAd():


# testing that country temperatures are updated
def test_country_temperatures():
    # update while temperature does not exceed max temperature
    # exception raised when
    with pytest.raises(Exception):
        pass


# testing that the report is displayed in desired manner
def test_report():
    pass




