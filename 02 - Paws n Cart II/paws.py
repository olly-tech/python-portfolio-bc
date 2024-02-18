# Divider line set to terminal width
import os
os_width = os.get_terminal_size().columns
line = "-" * os_width

# item array iterated through using for loop
pet_items = ["catnip", "dog leash", "fish food", "bird seeds", "hamster wheel"]

for item in pet_items:
    print(item.title())

# empty cart list
cart = []

error = "ERROR: please try again"

# while loop to add/remove item until finished
while True:
    user_input = input(f"""{line}
Enter:
    'add' to add an item
    'remove' to remove an item
    'done' when you are finished.

""")
    if "done" in user_input.lower(): # end loop
        break
    elif "add" in user_input.lower(): # add item
        # user views items they can add
        for item in pet_items:
            print(item.title())
        # user adds item
        add_item = input("Enter the item you would like to add:\t")
        if add_item.lower() in pet_items:
            # user selects quantity and cart is extended
            quantity_count = int(input("How many would you like to add?\t"))
            cart.extend([add_item]* quantity_count)
        else:
            print(error)
    elif "remove" in user_input.lower():
        #check if cart has items in
        if cart:
            #show quantity of items in cart
            for item in pet_items:
                if item in cart: #only prints items if in cart
                    print(f"{item.title()}\tx{cart.count(item)}");
            #remove item from cart
            remove_item = input("Enter the item you would like to remove:\t")
            if remove_item.lower() in cart:
                cart.remove(remove_item)
            else:
                print(error)
        else:
            print("Your cart is empty.")
    else:
        print(error)


# ITEM VARIABLES AND EMPTY CART
# item1 = "Whiskers Cat Food"
# item2 = "Kong"
# item3 = "Lucerne Hay"
# item4 = "Fish Food"

# cart = ""

# item1_price = 1
# item2_price = 2.50
# item3_price = 0.30
# item4_price = 4.10

# # user views of item menu formatted correctly
# item_menu = f"""1. {item1}: £{item1_price:.2f}
# 2. {item2}:              £{item2_price:.2f}
# 3. {item3}:       £{item3_price:.2f}
# 4. {item4}:         £{item4_price:.2f}"""

# ## USER WELCOME MESSAGE ##
# print("Hello!\nWelcome to the Paws n Cart shopping service.")

# ## WHILE LOOP ##
# # non-nested while loop forms overall structure of menu, directing user back to menu selection
# done = False #sentinel value for while loop
# while not done:
#     #counting items in cart and cart view formatting
#     item1_count = cart.count(f"{item1}")
#     item2_count = cart.count(f"{item2}")
#     item3_count = cart.count(f"{item3}")
#     item4_count = cart.count(f"{item4}")
#     cart_view = f"""{line}
#     Your cart:\n
#     {item1} x {item1_count}
#     {item2} x {item2_count}
#     {item3} x {item3_count}
#     {item4} x {item4_count}"""

#     #main menu print
#     print(f"{line}"
#           "\nMain Menu:\n\n"
#           "1. View cart\n"
#           "2. Add item to cart\n"
#           "3. Remove item from cart\n"
#           "4. Calculate cost of cart\n\n"
#           "5. Finished\n"
#           f"{line}")
#     menu_selection = int(input("Enter the menu number of your selection:\t")) #main menu selection
#     #if/else statements direct user to correct process for the selection made.
#     if menu_selection == 1: #view cart
#         print(cart_view)
#     elif menu_selection == 2: #add item
#         done_item = False #sentinel value for editing cart
#         while not done_item:
#             # display menu to user at start of loop - user inputs number corresponding to menu.
#             print(f"{line}\nWhich item would you like to add?\n{item_menu}\n5. Finished\n")
#             item_selection = int(input("Enter item number to add:\t"))
#             #if/else statements add correct item to cart
#             if item_selection == 1:
#                 cart += item1
#             elif item_selection == 2:
#                 cart+=item2
#             elif item_selection == 3:
#                 cart+=item3
#             elif item_selection == 4:
#                 cart+=item4
#             elif item_selection == 5: #sends user back to main menu
#                 done_item = True
#             else: #error fallback
#                 print("ERROR")
#     elif menu_selection == 3: #remove item
#         done_item = False #sentinel value for editing cart
#         while not done_item:
#             # display menu to user at start of loop - user inputs number corresponding to menu.
#             print(f"{line}\nWhich item would you like to remove?\n{item_menu}\n\n5. Finished\n")
#             item_selection = int(input("Enter item number to remove:\t"))
#             #if/else statements remove correct item from cart
#             if item_selection == 1:
#                 cart = cart.replace(f"{item1}", "", 1)
#             elif item_selection == 2:
#                 cart = cart.replace(f"{item2}", "", 1)
#             elif item_selection == 3:
#                 cart = cart.replace(f"{item3}", "", 1)
#             elif item_selection == 4:
#                 cart = cart.replace(f"{item4}", "", 1)
#             elif item_selection == 5: #sends user back to main menu
#                 done_item = True
#             else: #error fallback
#                 print("ERROR")
#     elif menu_selection == 4 or menu_selection == 5: #calculate cost
#         print(cart_view) #show current cart to user
#         #calculate total by multiplying price with item count
#         item1_total = item1_count * item1_price
#         item2_total = item2_count * item2_price
#         item3_total = item3_count * item3_price
#         item4_total = item4_count * item4_price
#         cart_cost = item1_total + item2_total + item3_total + item4_total

#         print(f"\nYour cart is currently at £{cart_cost:.2f}") #total cost printed
#         if menu_selection == 5: #finished
#             done = True; #ends while loop
#     # elif menu_selection == 5: #finished
#     #     done = True #ends while loop
#     else: #other int input fallback
#         print("ERROR CODE")

# #end message
# print("\nThank you for shopping with Paws n Cart!")
# print(line)
