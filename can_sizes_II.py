
import math

class SteelCan:
    """
    A class representing a steel can.

    Attributes:
        name (str): The name of the can.
        radius (float): The radius of the can in centimeters.
        height (float): The height of the can in centimeters.
        cost (float): The cost per can in U.S. dollars.
    """

    def __init__(self, name, radius, height, cost):
        """
        Initializes a new instance of a SteelCan.

        Args:
            name (str): The name of the can.
            radius (float): The radius of the can in centimeters.
            height (float): The height of the can in centimeters.
            cost (float): The cost per can in U.S. dollars.
        """
        self.name = name
        self.radius = radius
        self.height = height
        self.cost = cost

    def compute_volume(self):
        """
        Computes the volume of the steel can.

        Returns:
            float: The volume of the can in cubic centimeters.
        """
        return math.pi * self.radius**2 * self.height

    def compute_surface_area(self):
        """
        Computes the surface area of the steel can.

        Returns:
            float: The surface area of the can in square centimeters.
        """
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def compute_storage_efficiency(self, volume, surface_area):
        """
        Computes the storage efficiency of the steel can.

        Returns:
            float: The storage efficiency of the can.
        """
        volume = self.compute_volume()
        surface_area = self.compute_surface_area()
        return volume / surface_area

    def compute_cost_efficiency(self):
        """
        Computes the cost efficiency of the steel can.

        Returns:
            float: The cost efficiency of the can.
        """
        volume = self.compute_volume()
        return volume / self.cost

def main():
    """
    Calculates and displays storage efficiency and cost efficiency for each can size.
    Identifies can sizes with the highest storage and cost efficiency.
    """
   
    can_sizes = [
        SteelCan("#1 Picnic", 6.83, 10.16, 0.28),
        SteelCan("#1 Tall", 7.78, 11.91, 0.43),
        SteelCan("#2", 8.73, 11.59, 0.45),
        SteelCan("#2.5", 10.32, 11.91, 0.61),
        SteelCan("#3 Cylinder", 10.79, 17.78, 0.86),
        SteelCan("#5", 13.02, 14.29, 0.83),
        SteelCan("#6Z", 5.40, 8.89, 0.22),
        SteelCan("#8Z short", 6.83, 7.62, 0.26),
        SteelCan("#10", 15.72, 17.78, 1.53),
        SteelCan("#211", 6.83, 12.38, 0.34),
        SteelCan("#300", 7.62, 11.27, 0.38),
        SteelCan("#303", 8.10, 11.11, 0.42)
    ]

    highest_storage_efficiency = 0
    highest_cost_efficiency = 0
    best_storage_can = None
    best_cost_can = None

    for can in can_sizes:
        radius = can["radius"]
        height = can["height"]
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)

        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can["cost"])

        print(f"Can: {can['name']}, Storage Efficiency: {storage_efficiency:.2f}, Cost Efficiency: {cost_efficiency:.2f}")

        if storage_efficiency > highest_storage_efficiency:
            highest_storage_efficiency = storage_efficiency
            best_storage_can = can["name"]

        if cost_efficiency > highest_cost_efficiency:
            highest_cost_efficiency = cost_efficiency
            best_cost_can = can["name"]

    print(f"\nThe can with the highest storage efficiency is: {best_storage_can}, with an efficiency of {highest_storage_efficiency:.2f}")
    print(f"The can with the highest cost efficiency is: {best_cost_can}, with an efficiency of {highest_cost_efficiency:.2f}")

if __name__ == "__main__":
    main()

