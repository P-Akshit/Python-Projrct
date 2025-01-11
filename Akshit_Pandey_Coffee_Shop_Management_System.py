import random
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="coffee_shop",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()


computer_name = "RoBoCoffee"
menu = ["Black Coffee", "Green Coffee", "Milk Coffee", "Latte", "Americano", "Cappuccino", "Espresso", "Arabica"]
priceofmenu = [120, 110, 70, 140, 190, 270, 150, 390]
payment = ("Cash", "Debit Card", "Credit Card", "PhonePay", "GooglePay", "UPI", "PayZapp")
cream_cost = 12

amount_status = "Paid"
print("Hi, I am " + computer_name + " a coffee shop robot")
print("Can I have your name for the order?")
user_name = input()
print("I am giving you the menu")
print(f"Welcome {user_name}! Here's the menu:")
for i, item in enumerate(menu):
    print(f"{i+1}. {item} - ₹{priceofmenu[i]}")
print("Now can you tell me your order?")
order = input().lower()

if order.title() in menu:
    print(f"{order.title()}? Right?")
    order_is_right = input().lower()
    if order_is_right == "yes":
        print("How much " + order + "\ndo you want")
        howmuch = input()

        print("Do,you want cream")
        cream = input()

        print("How will you pay?")
        pay_choice = input().title()

        if pay_choice.title() in payment:
            item_index = menu.index(order.title())
            total = int(howmuch) * priceofmenu[item_index]
            if cream.lower() == "yes":
                total += cream_cost

            print(f"\nYour total is ₹{total}.")
        
            order_date = datetime.now()

            data = (
                order_date,
                user_name,
                computer_name,
                order,
                "Yes" if cream == "yes" else "No",
                howmuch,
                pay_choice,
                total,
                amount_status
            )
            sql = "INSERT INTO coffee_order (order_date, customer_name, robo_name, coffee_type, cream_yes_or_no, quantity_of_coffee, payment_mode, total_amount, amouunt_paid_or_not_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, data)
            mydb.commit()

            print("Order placed successfully!")
        else:
            print("Invalid payment choice.")
else:
    print("Sorry, we do not have " + order + " here.")
    print("Please order from our menu.")