from simulator import *
from policies import *

def test_year():
    s = Simulator()
    assert s.year == 0
    s.advance_year()
    assert s.year == 1


