# product_name = "Laptop"
# quantity = 3
# unit_price = 2500.00

# total_revenue = quantity * unit_price

# print("Product:", product_name)
# print("Quantity:", quantity)
# print("Total revenue:", total_revenue)

# revenue = total_revenue

# if revenue > 5000:
#     print("Revenue is above the target.")
# else:
#     print("Revenue is at or below the target.")

def calculate_revenue(quantity, unit_price):
    return quantity * unit_price

print(calculate_revenue(3, 2500))
print(calculate_revenue(2, 100))