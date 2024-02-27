## import libraries ##
import os
import textwrap

## text attributes
OFF = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

# divider line
os_width = os.get_terminal_size().columns #sets to terminal width
line = "-" * os_width
#####

def welcome():
    """Displays welcome information"""

    welcome_info = '''
Welcome to the Simple Scribe!
HOW TO USE:
1. Type whatever you would like.
2. View what you have typed.
3. Enter the edit menu where you can make changes to your text.
'''
    print(f"{line}{welcome_info}{line}") #f-string needed for trailing whitespace

def display_text(user_text):
    """Display user's text"""
    print(f"{line}\n{textwrap.fill(user_text, os_width)}\n{line}")

def find_text(user_text):
    find = input("Find:\t")
    if find not in user_text:
        raise ValueError(f"{find} not found in text.")
    else:
        print(f"{find} is in your text {user_text.count(find)} times.")
    return find

def replace_edit(user_text):
    """Allow user to find and replace text."""
    while True:
        find = find_text(user_text)
        replace_quantity = int(input("""
Please select an option:
1 - Replace only the first instance.
2 - Replace ALL instances.
3 - Go back to 'find'.
"""))

        if replace_quantity == 1 or replace_quantity == 2:
            replace = input("Replace with:\t")
            if replace_quantity == 1:
                user_text = user_text.replace(find, replace, 1) #only first instance
            else:
                user_text = user_text.replace(find, replace)
            break
        elif replace_quantity == 3:
            continue  
        else:
            raise ValueError("Option not recognized.")
    # Return the modified user_text after exiting the loop
    return user_text

def text_formatting(user_text):
    """Allow user to apply text formatting of choice"""
    find = find_text(user_text)
    format_menu = int(input("""
    Select a text formatting option:
    0 - Clear Bold, Italics or Underline effects.
    1 - Bold
    2 - Italics
    3 - Underline
    4 - Convert to uppercase
    5 - Capitalise first letter of all words
    6 - Convert to lowercase
    """))
    if format_menu == 0:
        user_text = user_text.replace(find, f"{OFF}{find}{OFF}")
    elif format_menu == 1:
        user_text = user_text.replace(find, f"{BOLD}{find}{OFF}")
    elif format_menu == 2:
        user_text = user_text.replace(find, f"{ITALIC}{find}{OFF}")
    elif format_menu == 3:
        user_text = user_text.replace(find, f"{UNDERLINE}{find}{OFF}")
    elif format_menu == 4:
        user_text = user_text.replace(find, find.upper())
    elif format_menu == 5:
        user_text = user_text.replace(find, find.title())
    elif format_menu == 6:
        user_text = user_text.replace(find, find.lower())
    else:
        raise ValueError("Option not recognised.")
    return user_text


## main menu and running function
def main_menu():
    welcome()
    user_text = input("Please begin typing:\n")
    while True:
        display_text(user_text)
        try:
            edit_menu = int(input("""
1 - find and replace
2 - text formatting (bold, underline, italicised, capitalize)
3 - background and text colour
"""))

            if edit_menu == 1:
                user_text = replace_edit(user_text)
            elif edit_menu == 2:
                user_text = text_formatting(user_text)
            elif edit_menu == 3:
                pass # feature to be implemented
            else:
                raise ValueError("Option not recognized.")
        except ValueError as ve:
            print(f"ERROR: {ve} Please try again.")


if __name__ == "__main__":
    main_menu()
