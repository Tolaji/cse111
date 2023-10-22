# test_water_flow.py

import pytest
from pytest import approx
from water_flow import WaterVolume
water_tank = WaterVolume

# from WaterVolume import water_column_height
# from water_flow import pressure_gain_from_water_height 
# from water_flow import pressure_loss_from_pipe 
# from water_flow import pressure_loss_from_fittings 
# from water_flow import reynolds_number
# from water_flow import pressure_in_psi
# from water_flow import calculate_k
# from water_flow import pressure_loss_from_pipe_reduction

# def test_water_column_height():
#     water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)
#     """
#     Test cases for water_column_height function.
#     """
#     assert water_tank.water_column_height(0, 0) == approx(0)
#     assert water_tank.water_column_height(0, 10) == approx(7.5)
#     assert water_tank.water_column_height(25, 0) == approx(25)
#     assert water_tank.water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)
    """
    Test cases for pressure_gain_from_water_height function.
    """
    assert water_tank.pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert water_tank.pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert water_tank.pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)
    
def test_pressure_loss_from_pipe():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)
    """
    Test cases for pressure_loss_from_pipe function.
    """
    assert water_tank.pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert water_tank.pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert water_tank.pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert water_tank.pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert water_tank.pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert water_tank.pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert water_tank.pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)
    

def test_pressure_loss_from_fittings():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)  

    # Test cases
    assert water_tank.pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert water_tank.pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert water_tank.pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert water_tank.pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert water_tank.pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)



def test_reynolds_number():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)

    # Test cases
    assert water_tank.reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert water_tank.reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert water_tank.reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert water_tank.reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert water_tank.reynolds_number(0.28687, 1.75) == approx(500318, abs=1)
    
def test_pressure_loss_from_pipe_reduction():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0) 

    # Test cases
    assert water_tank.pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert water_tank.pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert water_tank.pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_pressure_in_psi():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)  

    # Test cases
    assert water_tank.pressure_in_psi(0) == approx(0)
    assert water_tank.pressure_in_psi(50) == approx(7.251887774, abs=0.001)
    assert water_tank.pressure_in_psi(100) == approx(14.50375555, abs=0.001)
    assert water_tank.pressure_in_psi(200) == approx(29.0075111, abs=0.001)
    assert water_tank.pressure_in_psi(500) == approx(72.51877774, abs=0.001)


def test_calculate_k():
    water_tank = WaterVolume(tower_height=10.0, tank_height=5.0)  

    # Test cases
    assert water_tank.calculate_k(80069, 0.048692, 0.048692) == approx(0.1, abs=0.001)
    assert water_tank.calculate_k(471729, 0.28687, 0.048692) == approx(0.5302, abs=0.001)
    assert water_tank.calculate_k(500318, 0.28687, 0.048692) == approx(0.5549, abs=0.001)

if __name__ == '__main__':
    pytest.main(["-v", "--tb=line", "-rN", __file__])