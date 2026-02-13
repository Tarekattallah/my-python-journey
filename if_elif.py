"""
This task demonstrates:
- Basic if condition
- Boolean values
- if-else statements
- Email and password validation
"""



# =========================
# Basic If Conditions
# =========================

Egypt = "egypt"

if Egypt == "egypt":
    print("Egypt is a country in Africa")


# =========================
# Boolean Example
# =========================

Egypt = True

if Egypt:
    print("Egypt is a country in Africa")


# Making it False
Egypt = False

if not Egypt:
    print("Egypt is a country in Africa")


# =========================
# If - Else Example
# =========================

Egypt = "egypt"

if Egypt == "egypt":
    print("egypt")
else:
    print("not egypt")


# =========================
# Check Email and Password
# =========================

DATABASE_EMAIL = "ahmed@gmail.com"
DATABASE_PASSWORD = "12345"


def validate_user(email, password):
    if email == DATABASE_EMAIL and password == DATABASE_PASSWORD:
        print("Validation successful")

    elif email != DATABASE_EMAIL and password == DATABASE_PASSWORD:
        print("Invalid email")

    elif email == DATABASE_EMAIL and password != DATABASE_PASSWORD:
        print("Invalid password")

    else:
        print("Both email and password are incorrect")


email = input("Please enter your email: ")
password = input("Please enter your password: ")

validate_user(email, password)
