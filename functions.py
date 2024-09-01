def calculate_discount(price, discount_percent):

    if discount_percent >= 20:

        calculated_discount = price * (discount_percent/100)

        final_price = price - calculated_discount
    
    else:

        final_price = price

    return final_price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

print(f"The final price is KES {final_price}")