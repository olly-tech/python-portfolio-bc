# Paws n Cart II - The Dynamic Shopping Cart Application
An upgrade on the shopping cart application to increase dynamicism and improve overall UX. 

## Project Description
This application was upgraded as part of the Hyperion Dev Software Engineering Bootcamp and had the following requirements:
1. Dynamic item addition/removal using `while` loops.
2. Efficient item display and management with `for` and nested loops. 
3. Robust handling of user input and cart modifications.
4. Modifying application to include list manipulations where more efficient.

This app showcases my knowledge and usage of Python Loops:
- For Loops
- While Loops
- Nested Loops
- Controlling Loop Execution

### Challenges and Fixes
Initially struggled to match the user input with the array as the case sensitivity with `.capitalize()` and `.lower()` methods weren't working with multiple word item names. Used PEP8 documentation to identify the `.title()` which fixed this issue. 

Fixed problem where appending quantity of items in cart created list in a list, by changing `.append` to `.extend`

## Next Steps and Future Features
- [ ] Add item prices and calculations for checkout.
- [ ] Build upon cart functionality to enable users to modify the quantity of items in their cart.
- [ ] Fix cart output to better align as currently catnip's quantity does not align with the other items'. 