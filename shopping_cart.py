# shopping_cart.py
# Annabelle Zebrowski
# OPIM 243 
# 02/24/2021
# Professor Rossetti 

# REQUIREMENTS
# A grocery store name of your choice 
# A grocery store phone number and/or website URL and/or address of choice
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
# The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
# The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
# A friendly message thanking the customer and/or encouraging the customer to shop again

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired output

# prints all of the products 
print(products)

total_price = 0
# set to zero so that prices can be added as the user inputs items 
selected_ids = []
# empty list so we can later print a list of the selected products 

while True:
# allows the user to look up multiple products

    # ask the user for product identifiers to match with the ids above 
    selected_id = input("Please input a product identifier (corresponding number between 1 and 20). When you are complete, type DONE: ")
    #print(selected_id) -- used while I practiced the code to make sure the input was printed correctly
    #print(type(selected_id)) -- lets us know what type user input is (e.g., str)
    #selected_id = int(selected_id) -- converts str to int

    #> "DONE" -- the user has no more products to purchase
    if selected_id == "DONE":
         break 
         # breaks out of the loop, as opposed to giving an error message
    else:
        selected_ids.append(selected_id)
        # adds each selected product to a running list 

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
    # 

print("-------------------------")
print("TRADER JOE'S GLOVER PARK")
print("https://www.traderjoes.com/")
print("-------------------------")
print("CHECKOUT AT: 2021-02-20 3:44 PM")
print("-------------------------")
print("SELECTED PRODUCTS:")
# information display for the user 
# print(selected_ids)
for selected_id in selected_ids:
    # look up information about products with the given identifiers
    matching_products = [item for item in products if str(item["id"]) == str(selected_id)]
    # converts the user input and the product ID as type string 
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    # adds each price to a running total of the prices 
    print(str(matching_product["name"]) + " " + (to_usd(matching_product["price"])))
    # prints all of the products that were purchased along with their prices 
print("-------------------------")
# subtotal of products before taxes 
subtotal = str(total_price)
print("SUBTOTAL: " + to_usd(float(subtotal)))
# calculating sales tax using NYC's rate of 8.75% 
sales_tax = float(subtotal) * 0.0875
print("TAX: ", to_usd(sales_tax))
# total including prices for the customer to see  
price_total = sales_tax + float(subtotal)
print("TOTAL: " + to_usd(price_total))
print("-------------------------")
print("THANK YOU! WE HOPE TO SEE YOU SOON!")
print("-------------------------")