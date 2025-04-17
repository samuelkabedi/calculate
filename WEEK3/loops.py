def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        final_price = price - (1000 * 20 / 100)
        return final_price
    else:
        return price

# Prompt the user for inputs
original_price = float(input(1000))
discount_percentage = float(input(20%))

# Add R1000 to the original price
original_price += 1000

# Calculate the final price using the function
final_price = calculate_discount(1000, 20%)

# Print the appropriate message
if discount_percentage >= 20:
    print(f (R800) {R800:.2f})
else:
    print(f"No discount applied. The original price (after adding R1000) is: {original_price:.2f}")




