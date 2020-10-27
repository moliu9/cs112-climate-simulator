from policies import *
import pytest


def test_baseline():
    # constant non-zero emission
    assert Baseline(0.1).emit(0,1) == .1
    # zero emission
    assert Baseline(0).emit(2,9) == 0


def test_reducing():
    # if the emission is below zero, make the emissions zero
    assert Reducing(0, 5).emit(0,1) == 0
    # if the reducing increment is greater than baseline increase
    assert Reducing(3, 5).emit(0,1) == 0
    # if the emissions are above zero
    assert Reducing(6, 5).emit(0,1) == 1


def test_temperature_panic():
    # if temp is lower than threshold
    assert TemperaturePanic(3, 5, 5).emit(1, 6) == 3
    # if temp is higher than the threshold
    assert TemperaturePanic(10, 5, 3).emit(10, 1) == 7
    # if emissions fall below zero
    assert TemperaturePanic(3, 5, 5).emit(10, 1) == 0


def test_neighbor_average():
    # if emissions are higher than the neighboring countries, the country will reduce emission
    assert NeighborAverage(33, 5).emit(1,15) == 28
    # if emissions fall below zero
    assert NeighborAverage(33, 35).emit(1,15)  == 0
    # if emissions are lower than the neighboring countries, the country will continue to emmit at a constant rate
    assert NeighborAverage(3, 35).emit(1,15)  == 38



