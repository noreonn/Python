# Prompting the user to choose tariff type
tariff_type = int(input("Choose your tariff type 1-4: "))

# Prompting user for usage details
minutes = int(input("How many minutes have you used: "))
texts = int(input("How many texts have you sent: "))

# Initializing variables
monthly_cost = 0
free_minutes = 0
free_texts = 0
total_cost_of_texts = 0
total_cost_of_minutes = 0
total_bill_cost = 0

# Determining tariff details based on user input
if tariff_type == 1:
    monthly_cost = 10
    free_minutes = 75
    free_texts = 250
elif tariff_type == 2:
    monthly_cost = 15
    free_minutes = 150
    free_texts = 250
elif tariff_type == 3:
    monthly_cost = 20
    free_minutes = 300
    free_texts = 300
elif tariff_type == 4:
    monthly_cost = 25
    free_minutes = 300
    free_texts = 0

# Calculating extra costs for minutes and texts if exceeded free allowance
if minutes > free_minutes:
    total_cost_of_minutes = (minutes - free_minutes) * 0.12
if texts > free_texts and tariff_type != 4:
    total_cost_of_texts = (texts - free_texts) * 0.07

# Displaying usage details
print(f"You were on your phone for {minutes} minutes")
print(f"You sent {texts} texts")

# Calculating total bill cost
total_bill_cost = total_cost_of_texts + total_cost_of_minutes + monthly_cost
print("\nThe total cost of your calls was", total_cost_of_minutes, "pounds")
print("And the cost of your texts was", total_cost_of_texts, "pounds")
print("The total cost of your bill was", total_bill_cost, "pounds")
