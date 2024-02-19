# Divider line set to terminal width
import os
os_width = os.get_terminal_size().columns
line = "-" * os_width

# set arrays and empty arrays for pet products, prices and cart items, quantities and price
pet_items = ["catnip", "dog leash", "fish food", "bird seeds", "hamster wheel"]
pet_prices = [2.50, 3, 1.20, 0.25, 10]
cart = []
cart_quantities = [] 
cart_price = 0

error = "ERROR: please try again" # error fallback

## USER WELCOME MESSAGE AND PRODUCTS SHOWN
print(f"{line}\nHello!\nWelcome to the Paws n Cart shopping service.")

# while loop for menu to add/remove item until checkout
while True:
    # print cart with item, quantity and item price
    i = 0
    if cart: #stop printing cart table headings if empty.
        print(f"{line}\n\033[1m\t\tCART\t\t\nItem\t\tPrice\tQuantity\033[0m") #checkout table headings
    else:
        print(f"{line}\nYour cart is empty.")
    for item in pet_items:
        if item in cart:
            if i == 0: #add extra \t to catnip to fix formatting issue
                print(f"{item.title()}\t\t£{pet_prices[i]:.2f}\tx{cart.count(item)}")
            else:
                print(f"{item.title()}\t£{pet_prices[i]:.2f}\tx{cart.count(item)}")
        # cart_price += pet_prices[i] * cart.count(item)
        i += 1
    # user input to add/remove items
    user_input = input(f"""{line}
Enter:
    'add' to add an item
    'remove' to remove an item
    'done' to checkout.

""")
    if "done" in user_input.lower(): # end while loop
        break
    elif "add" in user_input.lower(): # add item
        # user views items they can add
        i = 0
        print(line)
        for item in pet_items: #print item and price
            if i == 0:
                print(f"\t{item.title()}\t\t£{pet_prices[i]:.2f}")
            else:   
                print(f"\t{item.title()}\t£{pet_prices[i]:.2f}")
            i += 1
        # user adds item
        add_item = input("\nEnter the item you would like to add:\t")
        if add_item.lower() in pet_items:
            # user selects quantity and cart is extended
            quantity_count = int(input("How many would you like to add?\t"))
            cart.extend([add_item]* quantity_count)
        else:
            print(error)
    elif "remove" in user_input.lower():
        #check if cart has items in
        if cart:
            #remove quantity of item from cart
            remove_item = input("Enter the item you would like to remove:\t")
            if remove_item.lower() in cart:
                for item in pet_items: #prints quantity of item by iterating through for loop
                    if remove_item.lower() == item:
                        current_cartquant = cart.count(item)
                        remove_quantity = int(input(f"You have {current_cartquant} in your cart.\nHow many would you like to remove?\t"))
                if remove_quantity <= current_cartquant: #fallback if user tries removing items beyond cart quantity.
                    for i in range(remove_quantity): #removing multiple items from cart
                        cart.remove(remove_item)
                    if remove_quantity == current_cartquant:
                        print(f"{line}\n{remove_item.title()} has been removed from the cart.")
                else:
                    print(error)
            else:
                print(error)
        else:
            print("Your cart is empty.")
    else:
        print(error)

# total cart price and end checkout 
i = 0
for item in pet_items:
    cart_price += pet_prices[i] * cart.count(item)
    i += 1

print(f"{line}\nTotal Price: £{cart_price:.2f}") #Total cart price
print(f"Thank you for shopping at Paws n Cart!\n{line}")


