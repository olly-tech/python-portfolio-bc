# user input validations for career application

# inputs = full name, age, email, phone number - set false variables for while loops
name = False
age = False
email = False
phone = False

while True:
    ## full name input and validation
    while name == False:
        try:
            uname = input("Please enter your full name:\t")
            if any(num.isdigit() for num in uname): #if integers in username
                raise ValueError("ERROR: Your name must not include digits.")
            elif " " not in uname: #if full name not inputted.
                raise ValueError("ERROR: please insert your full name.")
            else:
                print(f"Name ({uname.title()}) entered successfully.")
                name = True
        except ValueError as ve:
            print(ve)

    ## age input and validation
    while age == False:
        try:
            uage = int(input("Enter your age:\t"))
            if uage < 0: #negative number error fallback
                raise ValueError
            elif uage < 18 or uage > 110: #age criteria validation
                print("Unfortunately, your age does not fit the application's criteria. Thank you for your time.")
                quit() #stops individual from continuing application or trying to change age
            else:
                print(f"Age ({uage}) has been successfully entered.")
                age = True
        except ValueError:
            print("ERROR: Invalid characters entered.")

    ## email address input and validation      
    while email == False:
        try:
            uemail = input("Enter your email:\t")
            if " " in uemail:
                raise ValueError("ERROR: email should not contain spaces. Please try again.")
            elif "@" in uemail and "." in uemail:
                # insert email again to confirm it's correctly inputted by user.
                    confirm_uemail = input("Please confirm your email address:\t")
                    if uemail == confirm_uemail: #validate both entries match
                        print(f"Email address ({uemail})  successfully entered")
                        email = True
                    else:
                        raise ValueError("ERROR: Email address does not match. Please try again.")
            else:
                raise ValueError("ERROR: Your email address must include '@' and '.' Please try again.")
        except ValueError as ve:
            print(ve)

    ## phone number input and validation
    while phone == False:
        try:
            uphone = input("Enter your phone number:\t")
            if uphone[0] == "0" and len(uphone) == 11 and uphone.isdigit():
                print(f"Phone number ({uphone}) entered successfully")
                uphone = int(uphone)
                phone = True
            elif not uphone.isdigit():
                raise ValueError("ERROR: phone number must only contain digits.")
            elif len(uphone) != 11:
                raise ValueError("ERROR: phone number must contain 11 digits.")
            elif uphone[0] != "0":
                raise ValueError("ERROR: phone number must begin with 0")
            else:
                raise ValueError("ERROR: invalid number. Please try again.")
        except ValueError as ve:
            print(ve)

    try:
        confirm_info = input(f"""
    Please review your application form:
        Name: {uname.title()}
        Age: {uage}
        Email Address: {uemail}
        Phone Number: {uphone}

    Are these details correct?
        'y' - yes
        'n' - no

        """)
        if confirm_info == "y" or confirm_info == "'y'" or confirm_info == "yes":
            print("Thank you for entering your information. This program confirms your details pass the minimum  criteria.")
            break
        # menu to go back to change information
        elif confirm_info == "n" or confirm_info == "'n'" or confirm_info == "no":
            edit_form = int(input("""
    Which item would you like to edit?
        1 - Name
        2 - Age
        3 - Email Address
        4 - Phone Number
                            """))
            if edit_form == 1:
                name = False #goes back to earlier name while loop
            elif edit_form == 2:
                age = False
            elif edit_form == 3:
                email = False
            elif edit_form == 4:
                phone = False
            elif edit_form.isdigit():
                raise ValueError("ERROR: please select an option from 1-4")
            else:
                raise ValueError("ERROR: Please enter a number from the option.")     
        else:
            raise ValueError("ERROR: Choice not recognised. Please enter y or n")
    except ValueError as ve:
        print(ve)
