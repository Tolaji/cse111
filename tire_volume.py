
import math

class TireVolumeCalculator:
    #Define constructor
    def __init__(self, width, aspect_ratio, diameter):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.diameter = diameter
    
    #Define method to calculate tire volume
    def calculate_tire_volume(self):
        #Convert width to meters and diameter to centimeters
        #w = width / 1000
        #d = diameter
        
        #Calculate volume using the formula
        pi = math.pi
        volume = (pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
        return volume
        
#user inputs
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#Create instance of TireVolumeCalculator class
tire_volume_calculator = TireVolumeCalculator(width, aspect_ratio, diameter)

#Calculate tire volume
tire_volume = tire_volume_calculator.calculate_tire_volume()

#Print tire volume
print(f"The volume of the tire is {tire_volume:.2f} liters.")

