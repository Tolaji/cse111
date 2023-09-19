from math import ceil

class BoxesRequired:
    # Define Constructor
    def __init__(self, items_per_box, total_items):
        self.total_items = total_items
        self.items_per_box = items_per_box
    
    # Define function to calculate number of boxes needed
    def calculate_boxes(self):
        boxes_needed = ceil(total_items / items_per_box) #Calculate boxes needed precisely to the nearest whole number using 'ceil' instead of 'round' ensuring enough boxes to hold all items
        return boxes_needed

# Ask for user input
total_items = int(input("Enter the number of manufactured items: "))
items_per_box = int(input("Enter the number of items to pack per box: "))

# Create an instance of BoxesRequired class
boxes_calculator = BoxesRequired(items_per_box, total_items)

# Calculate boxes needed
boxes_needed = boxes_calculator.calculate_boxes()

# Print the result
print(f"The number of boxes necessary to hold the items is: {boxes_needed}")







# Get current day of the week from the operating system
current_day = get_current_day_of_week()

# Prompt the user for the subtotal
subtotal = input("Enter the subtotal: ")
subtotal = convert_to_float(subtotal)

# Check if it's Tuesday (1) or Wednesday (2), and subtotal is $50 or greater
if current_day == 1 or current_day == 2:
    if subtotal >= 50:
        # Apply 10% discount
        discount_amount = subtotal * 0.10
        subtotal = subtotal - discount_amount

# Calculate sales tax (6% of the subtotal)
sales_tax = subtotal * 0.06

# Calculate total amount due
total_due = subtotal + sales_tax

# Print the results
if discount_amount > 0:
    print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Sales Tax Amount: ${sales_tax:.2f}")
print(f"Total Amount Due: ${total_due:.2f}")



class Discount:
    @staticmethod
    def calculate_discount(subtotal):
        # Get the current day of the week from your computer's operating system
        # (This code assumes you are using Python's built-in `datetime` module)
        import datetime
        current_day = datetime.datetime.now().strftime("%A")

        # Check if the subtotal is $50 or greater and today is Tuesday or Wednesday
        if subtotal >= 50 and (current_day == "Tuesday" or current_day == "Wednesday"):
            discount = subtotal * 0.1
            subtotal -= discount
            print(f"Discount amount: ${discount:.2f}")

        # Compute the total amount due by adding sales tax of 6% to the subtotal
        sales_tax = subtotal * 0.06
        total_amount_due = subtotal + sales_tax

        # Print the sales tax amount and the total amount due
        print(f"Sales tax amount: ${sales_tax:.2f}")
        print(f"Total amount due: ${total_amount_due:.2f}")


# Example usage:
customer_subtotal = float(input("Enter customer's subtotal: "))
Discount.calculate_discount(customer_subtotal)

