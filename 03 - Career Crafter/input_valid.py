# user input validations for career application

# name entry and validation 
while True:
    user_fullname = input("Enter your full name\t")
    if " " in user_fullname:
        user_fullname = user_fullname.split(" ", 1)
        print("Name accepted.")
        break
    else:
        print("ERROR: please enter a forename and surname")

# email address and validation
while True:
    user_email = input("Enter your email\t")
    if "@" in user_email and "." in user_email:
        print("Email address accepted")
        break
    else:
        print("ERROR: email address invalid. Please try again.")

# phone number input and validation
while True:
    user_phoneno = input("Enter your phone number\t")
    if len(user_phoneno) == 11 and user_phoneno.isdigit():
        print("Phone number accepted")
    else:
        print("ERROR: invalid number. Please try again.")
        

# user_location = input("Enter your location\t")
# user_skills = input("Enter your skills\t")
# user_languages = input("Enter your programming language proficiencies\t")