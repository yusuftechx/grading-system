# Prompt the user to enter their username
username = input("Enter your username")

# Prompt the user to enter their password
password = input("Enter your password")

# Check if the entered username matches the expected username
if username == "Yusuftech":
    # If username is correct, check if the entered password matches the expected password
    if password == "12345":
        # Output a success message if both username and password are correct
        print("Login Successful")
    else:
        # Output an error message if the password is incorrect
        print("Invalid Password")
else:
    # Output an error message if the username is not found
    print("User Not Found")


# Prompt the user to input their grade marks as an integer
gradeMarks = int(input("Enter your Grade: "))

# Determine the grade based on the entered marks and print the result
if gradeMarks >= 90:
    # If marks are 90 or above, classify as 'Excellent'
    print("Grade - Excellent")
elif gradeMarks < 90 and gradeMarks >= 75:
    # If marks are between 75 and 89, classify as 'First Class'
    print("Grade - First Class")
elif gradeMarks < 75 and gradeMarks >= 40:
    # If marks are between 40 and 74, classify as 'Average'
    print("Grade - Average")
else:
    # If marks are below 40, classify as 'Fail'
    print("Grade - Fail")
