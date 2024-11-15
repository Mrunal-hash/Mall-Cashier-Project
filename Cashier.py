"""Cashier function in a mall consists of
1. Adding the items and its quantity
2. Calculating their sum
3. Calculating the discount if the customer is either a bronze, silver or gold member
(Bronze member - 5% discount
Silver member - 10% discount
Gold member - 20% discount)
"""

# Step 1: Create an inventory for available items
def inventory(product):
    product = [
        'MILK',
        "EGGS",
        "SPINACH",
        "POTATOES",
        "TOFU",
        "CHICKEN",
        "BREAD",
        "BUTTER",
        "CHEESE"]

    return product

# Step 2 - Create a function to add all the items and their respective quantity and verify if the items are available in the inventory
def groceryList():
    grocery_list = {}
    addItem = True
    while addItem:
        # input to add item or quit
        item = input("Would you like to add item? Press A to add an item, press Q to quit: ").upper()
        if item == 'A':
            # Enter the product name
            product = input("Enter product name: ").upper()\

            # Verify if the product is available in the inventory(product)
            if product not in inventory(product):
                print("Product not available. Add another!")
                pass
            else:
            # Add the quantity if product is available
                qty = int(input("Enter quantity: "))
                grocery_list.update({product:qty})

        elif item == 'Q':
        #If you don't want to add products any further
            addItem = False
        else:
        # If you select incorrect option
            print("Select correct option")
    # Returns a dictionary of product and it's quantity after addition
    return  grocery_list

#Step 3: Calculate the total after adding the items and their price
def getPrice(product, qty):
    price_list = {
        'MILK':2,
        "EGGS":1,
        "SPINACH":1,
        "POTATOES":2,
        "TOFU":3,
        "CHICKEN":4,
        "BREAD":2,
        "BUTTER":2,
        "CHEESE":2
    }
    subtotal = price_list[product] * qty

    print(product + ":$" + str(price_list[product]) + "x" + str(qty) + "=" + str(subtotal))
    # Returns the cost of the product
    return subtotal

#Step 4: Do a total sum of the list after discount

def getDiscount():
    membership = ''
    while membership not in ["BRONZE","SILVER","GOLD","NO"]:
        membership = input("Do you have a membership?(Gold, Silver or Bronze): ").upper()
    # Returns the discount for the membership if any
    if membership == 'BRONZE':
        return 0.05
    elif membership == 'SILVER':
        return 0.10
    elif membership == 'GOLD':
        return 0.20
    else:
        return 0

#Step 5: To repeat the next checkout
def replay():

    choice = input("Do you like to do another checkout? Yes/No: ").upper()
    # Returns to the start if you want to check out again
    return choice == 'YES' or choice == 'Y'

#Step 6: To create the cashier system

#Welcome statement
print("WELCOME TO THE MART!")

checkout = ''
# To check if the customer wants to checkout
while checkout != 'Y' and checkout != 'N':
    checkout = input("Are you ready to checkout? Y/N: ").upper()

if checkout == 'Y':
    proceed = True
else:
    proceed = False

while proceed:
    #add items in the grocery list
    print("Please enter your items to checkout!!")
    items = groceryList()

    #get the total of the bill
    total = 0
    for i in items:
        price = getPrice(i,items[i])
        total = total + price

    #Add discount to the bill if any
    discount = getDiscount()

    grand_total = total - round(total*discount,2)
        print("Your total is $" +str(total)+ ". Your total after discount is: $" +str(grand_total)+ ". You have saved $" + str(round(total*discount,2))+ " on your bill.")

    if not replay():
        print("***THANK YOU FOR SHOPPING WITH US!***")
        break
