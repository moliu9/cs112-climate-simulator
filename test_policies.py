from policies import *

def test_baseline():
    assert Baseline(0.1).emit(0,1) == .1
    assert Baseline(0).emit(2,9) == 0

def test_reducing():
    # If the emission is greater or equal to
    assert Reducing(0, 5).emit(0,1) == 0  #if the emissions are below zero, make
                                          #the emissions zero
    assert Reducing(3, 5).emit(0,1) == 0
    assert Reducing(6, 5).emit(0,1) == 1  #If the emissions are above zero
    assert Reducing(4, 5).emit(0,1) == 0

def test_temperature_panic():
    assert TemperaturePanic(3, 5, 5).emit(1,6) == 3    #if temp is lower than
                                                       #threshold
    assert TemperaturePanic(10, 5,3 ).emit(10,1) == 7  #if temp is higher than
                                                       #threshold
    assert TemperaturePanic(3, 5 ,5).emit(10,1) == 0   #if emissions fall
                                                       #below zero
    assert TemperaturePanic(3, 5, 4).emit(12,5) == 12   #normal case

def test_neighbor_Average():
   assert NeighborAverage(33, 5).emit(1,15) == 28  #if emissions are higher than
                                                   #the neighboring countries, the
                                                   #country will reduce emission

   assert NeighborAverage(33, 35).emit(1,15)  == 0  #if emissions fall
                                                    #below zero
   assert NeighborAverage(3, 35).emit(1,15)  == 38  #if emissions are lower than
                                                    #the neighboring countries,
                                                    #the country will continue
                                                    #to emmit at a constant rate



