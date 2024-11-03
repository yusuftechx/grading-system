username = input("Enter your username")
password = input("Enter your password")
if username == "Yusuftech":
    if password == "12345":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("User Not Found")

gradeMarks = int(input("Enter your Grade: "))
if gradeMarks >= 90:
    print("Grade - Excellent")
elif gradeMarks < 90 and gradeMarks >= 75:
    print("Grade - First Class")
elif gradeMarks < 75 and gradeMarks >= 40:
    print("Grade - Average")
else :
    print("Grade - Fail")
    # comment: 
            