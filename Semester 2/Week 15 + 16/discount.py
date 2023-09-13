from datetime import datetime

discount = 0.10
salestax = 0.06

#find discount amount
subtotal = float(input('Please enter the subtotal: '))
now = datetime.now()
weekday = now.weekday()
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = subtotal * discount
    print(f'Discount amount: {discount:.2f}')
    subtotal -= discount

#find sales tax
salestax = round(subtotal * salestax, 2)
print(f'Sales tax amount: {salestax:.2f}')

#find total
total = subtotal + salestax
print(f'Total: {total:.2f}')





subtotal = 0

print("Enter the price and quantity for each item.")
price = 1
while price != 0:
    # Get the price from the user.
    price = float(input("Please enter the price: "))
    if price != 0:
        # Get the quantity from the user.
        quantity = int(input("Please enter the quantity: "))

        subtotal += price * quantity

        # Print a blank line.
        print()

# Round the subtotal to two digits after
# the decimal and print the subtotal.
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

now = datetime.now()
weekday = now.weekday()

# if the subtotal is greater than 50 and today is
# Tuesday or Wednesday, compute the discount amount.
if weekday == 1 or weekday == 2:
    if subtotal < 50:
        lacking = 50 - subtotal
        print("To receive the discount, add"
                f" {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * discount, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount

sales_tax = round(subtotal * salestax, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: {total:.2f}")