## DIVIDER LINE ##
import os
os_width = os.get_terminal_size().columns #sets to terminal width
line = "-" * os_width

## TEXTWRAP AND TEXT ATTRIBUTES
import textwrap
OFF = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

# While loop variables
find_repl = False
text_format = False
bgfg_colour = False

# Welcome message and Tutorial
welcome_info = """
Welcome to the Simple Scribe!
HOW TO USE:
1. Type whatever you would like.
2. View what you have typed.
3. Enter the edit menu where you can make changes to your text.
"""

# User Input
user_text = input("Please begin typing.")

while True:
    # print text and present edit menu
    # text wrap keeps words together at terminal edges.
    print(f"""
{line}
{textwrap.fill(user_text, os_width)}
{line}
""")
    try:
        edit_menu = int(input("""
Select an option to edit your text.
    1 - find and replace
    2 - text formatting (bold, underline, italicised, capitalise)
    3 - background and text colour
"""))
        if edit_menu == 1:
            find_repl = True
        elif edit_menu == 2:
            text_format = True
        elif edit_menu == 3:
            bgfg_colour = True
        else:
            raise ValueError("Option not recognised.")
    except ValueError as ve:
        print(f"ERROR: {ve} Please try again.")
    
    

    # Find and Replace Tool
    while find_repl == True:
        try:
            find = input("Find:\t")
            if find not in user_text: #user error fallback
                raise ValueError(f"{find} not found in text.")
            else:
                print(f"{find} is in your text {user_text.count(find)} times.")
            replace = input("Replace:\t")
            replace_quantity = int(input("""
Please select an option:
    1 - replace only the first instance.
    2 - replace ALL instances.
    3 - go back to 'Find' something different.
"""))
            # replace only 1 instance
            if replace_quantity == 1:
                user_text = user_text.replace(find, replace, 1)
                find_repl = False
            # replace all
            elif replace_quantity == 2:
                user_text = user_text.replace(find, replace)
                find_repl = False
            # go back to find
            elif replace_quantity ==3:
                continue
            else:
                raise ValueError("Option not recognised.")
        except ValueError as ve:
            print(f"ERROR: {ve} Please try again.")
    
    # Text Formatting Tool
    while text_format == True:
        try:
            ## find text to edit
            find = input("Enter the text you would like to format:\t")
            if find not in user_text: #user error fallback
                raise ValueError(f"{find} not found in text.")
            print(f"{BOLD}{find}{OFF} is in your text {user_text.count(find)} times.\nThis program will edit all occurrences.")
            
            ## format menu
            format_menu = int(input("""
Select a text formatting option?
    0 - Clear Bold, Italics, Underline effects
    1 - Bold
    2 - Italics
    3 - Underline
    4 - Capitalise all
    5 - Capitalise first letter
    6 - Convert to lowercase
"""))
            if format_menu == 1:
                user_text = user_text.replace(find, f"{BOLD}{find}{OFF}")
            elif format_menu == 2:
                user_text = user_text.replace(find, f"{ITALIC}{find}{OFF}")
            elif format_menu == 3:
                user_text = user_text.replace(find, f"{UNDERLINE}{find}{OFF}")
            elif format_menu == 4:
                user_text = user_text.replace(find, find.capitalize())
            elif format_menu == 5:
                user_text = user_text.replace(find, find.title())
            elif format_menu == 6:
                user_text = user_text.replace(find, find.lower())
            elif format_menu == 0:
                user_text = user_text.replace(find, f"{OFF}{find}{OFF}")
            else:
                raise ValueError("Option not recognised.")
            text_format = False   
        except ValueError as ve:
            print(f"ERROR: {ve} Please try again.")