# water_flow.py

class WaterVolume:

    # Constants
    GRAVITY_ACCELERATION = 9.80665 # m/s^2
    WATER_DENSITY = 998.2 # kg/m^3
    WATER_VISCOSITY = 0.0010016 # kg/(ms)

    def __init__(self, tower_height, tank_height):
        self.tower_height = tower_height
        self.tank_height = tank_height

    def water_column_height(self):

        """
                Calculate the height of the water column in a tank.

                Parameters:
                    tower_height (float): Height of the tower.
                    tank_height (float): Height of the tank.

                Returns:
                    float: Height of the water column.
                """
        height = self.tower_height + (3 * self.tank_height / 4)
        
        print(f'Water Column Height is {height:.2f}')
        
        return height 


    def pressure_gain_from_water_height(self, height):
        """
                Calculate the pressure caused by Earth's gravity pulling on water in an elevated tank.

                Parameters:
                    height (float): Height of the water column in meters.

                Returns:
                    float: Pressure in kilopascals.
                """
        water_density = 998.2
        earths_gravity = 9.80665
        pressure = (water_density * earths_gravity * height) / 1000
        
        print(f'Pressure gain from water height is {pressure:.2f}')
        
        return pressure

    def pressure_loss_from_pipe(self, pipe_diameter, pipe_length, friction_factor, fluid_velocity):
        """
                Calculate the pressure loss due to friction within a pipe.

                Parameters:
                    pipe_diameter (float): Diameter of the pipe in meters.
                    pipe_length (float): Length of the pipe in meters.
                    friction_factor (float): Friction factor of the pipe.
                    fluid_velocity (float): Velocity of the water flowing through the pipe in meters/second.

                Returns:
                    float: Pressure loss in kilopascals.
                """
        water_density = 998.2
        pressure_loss = -(friction_factor * pipe_length * water_density * fluid_velocity**2) / (2000 * pipe_diameter)
        
        print(f'Pressure Loss from pipe is {pressure_loss:.2f}')
        
        return pressure_loss

    def pressure_loss_from_fittings(self, fluid_velocity, quantity_of_fittings):
        """
                Calculate pressure loss due to fittings.

                Parameters:
                    velocity (float): Velocity of the water flowing through the pipe in meters/second.
                    quantity_of_fittings (int): Quantity of fittings.

                Returns:
                    float: Pressure loss in kilopascals.
                """
        pressure_loss = (-0.04 * self.WATER_DENSITY * fluid_velocity**2 * quantity_of_fittings) / (2000)
        
        print(f'Pressure Loss from fittings is {pressure_loss:.2f}')
        
        return pressure_loss

    def reynolds_number(self, hydraulic_diameter, fluid_velocity):
        """
                Calculate Reynolds number.

                Parameters:
                    diameter (float): Hydraulic diameter of the pipe in meters.
                    velocity (float): Velocity of the water flowing through the pipe in meters/second.

                Returns:
                    float: Reynolds number.
                """
        reynolds_number = (self.WATER_DENSITY * hydraulic_diameter * fluid_velocity) / self.WATER_VISCOSITY
        
        print(f'Reynolds Number is {reynolds_number:.2f}')

        return reynolds_number
 

    @staticmethod
    def pressure_in_psi(pressure_kpa):
        """
                    Convert pressure from kilopascals to pounds per square inch (psi).
                    Parameters:
                        pressure_kpa (float): Pressure in kilopascals.
                    Returns:
                        float: Pressure in pounds per square inch.
                    """
        psi = pressure_kpa * 0.14503773773375 # 1 kPa = 0.14503773773375 psi
        
        print(f'Psi is {psi:.2f}')
        
        return psi

    def calculate_k(self, Reynolds_number, D, d):
        """
                    Calculate the constant 'k' used in the pressure loss formula.
                    Parameters:
                        Reynolds_number (float): Reynolds number of the larger diameter pipe in meters.
                        d (float): Diameter Diameter of the smaller pipe in meters.
                    Returns:
                        float: Constant 'k'.
                    """
        k = (0.1 + (50 / Reynolds_number)) * ((D / d)**4 *(- 1))
        k = (0.1 + (50/Reynolds_number))*((D/d)**4 - 1)
        
        print(f"Constant 'K' is {k:.2f}")
        
        return k

    def pressure_loss_from_pipe_reduction(self, Reynolds_number, D, d, fluid_velocity):
        """
                    Calculate pressure loss due to a rounded reduction in the pipe's diameter.
                    Parameters:
                        Reynolds_number (float): Reynolds number of the larger diameter pipe.
                        D (float): Diameter of the larger pipe in meters.
                        d (float): Diameter of the smaller pipe in meters.
                        velocity (float): Velocity of the water flowing through the larger diameter pipe in meters/second.
                    Returns:
                        float: Pressure loss in kilopascals.
                    """
        k = self.calculate_k(Reynolds_number, D, d)
        pressure_loss = -(k * self.WATER_DENSITY * fluid_velocity**2)/2000
        
        print(f'Pressure loss from pipe reduction is {pressure_loss:.2f}')
        
        return pressure_loss
    
    

def main():
    
    print("\nWater Volume Calculations")
    print('-'*70)
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    print('\nReturned Parameters')
    print('-'*70)
    
    water_tank = WaterVolume(tower_height, tank_height)
    water_height = water_tank.water_column_height()
    pressure = water_tank.pressure_gain_from_water_height(water_height)
    
    PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
    PVC_SCHED80_FRICTION_FACTOR = 0.013 # (unitless)
    SUPPLY_VELOCITY = 1.65 # (meters / second)
    
    HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
    HDPE_SDR11_FRICTION_FACTOR = 0.018 # (unitless)
    HOUSEHOLD_VELOCITY = 1.75 # (meters / second)
        
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    
    reynolds = water_tank.reynolds_number(diameter, velocity)
    
    
    loss = water_tank.pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = water_tank.pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = water_tank.pressure_loss_from_pipe_reduction(diameter,
        velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss =water_tank.pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print()
    print('-'*70)
    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()