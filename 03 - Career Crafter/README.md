# Career Crafter - Validating User Input Program
A program that allows a user to enter their personal information for an application and validates the input against a specific criteria.

## Project Description
This application was created as part of the Hyperion Dev Software Engineering Bootcamp and had the following requirements:
1. Use conditional statements for input validation.
2. Use try-except blocks to gracefully manage unexpected exceptions.
3. Recognise and address various error types, including edge cases.

This program will take input from user related to an application form. These inputs will be validated, and cleaned prior to processing. Predictable user errors and edge cases will be handled. The following inputs will be focused on: full name, phone number, email, age.

As such, this program showcases my knowledge and usage of Python:
- Conditional statements
- Try-Except
- Error Types

### Specific and Additional Features
Played with the project's objectives to increase challenge and programming learning. Each input was contained in a while loop with a boolean-constrained variable. The inputs were validated and made user-friendly in the following ways:
- Full Name
    - used `any` function to identify if integers had been inputted anywhere in string.
    - identified if only one name had been inputted by searching for whitespace.
- Age
    - included parameters for age to showcase terminating programs early when necessary. Individuals outside of the age range will be exited from the program. This will reduce the number of users that input a different age to bypass the restriction.
    - created error handling for negative numbers as well as non-numbers
- Email Address
    - created error handling for email addresses that do not include "@" or ".", or have whitespace in.
    - inserted a confirmation of email process to ensure users input the correct email.
- Phone Number
    - included parameters for numbers that weren't the right length or didn't start with 0 as is typical in the UK. 
- Confirmation Menu
    - created this to ensure users had the opportunity to edit prior answers. While loop and Boolean values redirect users in the most efficient way. This means user only has to edit the one portion rather than their whole form.

## Additional Features and Future Steps
- [ ] Allow users to set up their own application conditions that the applicant's data should adhere to.
- [ ] Refactor code for optimisation and readability
