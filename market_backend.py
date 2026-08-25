# The Problem: Store Checkout System
# You are building a backend system for a local grocery store. You are provided with a raw list of newly arrived inventory items. Each item in the list is a tuple containing (product_name, price, quantity). 
# Your goal is to process this raw data, build a structured inventory, check product availability, and generate a customer receipt.
# Given Input Data
# Copy this raw list into your Python environment:
# # Raw stock delivery data
# raw_delivery = [
#     ("Apple", 0.75, 50),
#     ("Banana", 0.40, 100),
#     ("Milk", 2.50, 15),
#     ("Bread", 1.80, 20),
#     ("Apple", 0.75, 30),  # Extra stock of apples arriving
# ]

# # Customer shopping cart (List of products they want to buy)
# shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]
# Your Tasks
# 1.	Build the Inventory (Dictionary):
# Write a function to convert the raw_delivery list of tuples into a dictionary.
# o	The keys must be the product names.
# o	The values must be another dictionary containing {"price": float, "stock": int}.
# o	Note: If a product appears more than once in the raw data (like "Apple"), sum up its stock quantities.
# 2.	Process the Shopping Cart:
# Iterate through the shopping_cart list. Check your inventory dictionary for each item:
# o	If the item exists and is in stock, decrease its stock by 1 and record the sale.
# o	If the item exists but is out of stock, print a message: "[Product] is sold out!".
# o	If the item does not exist in the inventory, print a message: "[Product] is not carried in this store". 
# 3.	Generate the Receipt (Tuple & List):
# Create a list of tuples representing the customer's final receipt. Each tuple should be structured as (product_name, price). Print out the total price at the end.


raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
 ]

shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]


# Raw stock delivery data
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30)
]

# Customer shopping cart
shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]


# --------------------------------------------------
# 1. BUILD INVENTORY
# --------------------------------------------------

def build_inventory(raw_delivery):

    inventory = {}

    for product, price, quantity in raw_delivery:

        if product in inventory:
            # Product already exists, so add the new stock
            inventory[product]["stock"] += quantity

        else:
            # Product doesn't exist, so create it
            inventory[product] = {
                "price": price,
                "stock": quantity
            }

    return inventory


# Build the inventory
inventory = build_inventory(raw_delivery)

print("Inventory:")
print(inventory)


# --------------------------------------------------
# 2. PROCESS SHOPPING CART
# --------------------------------------------------

receipt = []

for item in shopping_cart:

    # Check whether product exists
    if item not in inventory:
        print(item, "is not carried in this store")

    # Product exists
    elif inventory[item]["stock"] == 0:
        print(item, "is sold out!")

    # Product exists and is available
    else:
        # Decrease stock by 1
        inventory[item]["stock"] -= 1

        # Get price
        price = inventory[item]["price"]

        # Add product and price to receipt
        receipt.append((item, price))


# --------------------------------------------------
# 3. GENERATE RECEIPT
# --------------------------------------------------

print("\nReceipt:")

total = 0

for product, price in receipt:

    print(product, "-", price)

    total += price


print("Total price:", total)