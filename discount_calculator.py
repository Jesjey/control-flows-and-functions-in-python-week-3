def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
    
    Returns:
        float: The final price after applying the discount if
               discount_percent >= 20, otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# --- Main Program ---
# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"Final Price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
