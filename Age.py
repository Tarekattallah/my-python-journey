# The user give his age and calculate the days he has lived and hourse he has lived.

def cale_age(age):
    return "your age in dayes is " + str(age*365) + " and your age in hours is " + str(age*365*24)# get user input for age age = int(input("Please enter your age: ")) print(cale_age(age))
print(cale_age(int(input("Please enter your age: "))))



#Best practices for the above code:
def cala_age(age):
    # calculate the number of days lived
    print("your days lived is ",str(age*365))
    # calculate the number of hours lived
    print("your hours lived is ",str(age*365*24))
# get user input for age
age = int(input("Please enter your age: "))
cala_age(age)


