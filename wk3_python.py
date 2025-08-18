def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Only applies the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        print(f"The final price after {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
