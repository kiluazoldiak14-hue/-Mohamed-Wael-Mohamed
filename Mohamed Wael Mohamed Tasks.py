# Define prices of three items
item1_price = 40
item2_price = 35
item3_price = 25

# Define the budget
budget = 120

# Calculate total cost
total_cost = item1_price + item2_price + item3_price

# Print total cost and budget
print("Total cost:", total_cost)
print("Budget:", budget)

# Compare total cost with the budget
difference = budget - total_cost

if difference > 0:
    print("Money left:", difference)
elif difference < 0:
    print("Money needed:", abs(difference))
else:
    print("The budget is exactly enough.")