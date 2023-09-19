"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""


#Function to calculate Maximum Heart Rate (MHR)
def calculate_max_heart_rate(age):
    max_heart_rate = 220 - age
    return max_heart_rate

#Function to determine Target Heart Rate Range
def determine_target_heart_rate_range(max_heart_rate):
    lowerRange = 0.65 * max_heart_rate
    upperRange = 0.85 * max_heart_rate
    return lowerRange, upperRange

#function to get user age input
def get_user_age(self):
    self.age = int(input("Please enter your age: "))
    
    

#Example Usage

age = get_user_age()
max_heart_rate = calculate_max_heart_rate(age)
lowerRange, upperRange = determineTargetHeartRateRange(max_heart_rate)

print("Your target heart rate range is between", lowerRange, "and", upperRange)


text = input("Please enter your name: ")
color = input("What is your favorite color? ")

print(f"Heart rate: {rate}")

