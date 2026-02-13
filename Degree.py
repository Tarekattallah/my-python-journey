"""
This program compares the degrees of three students
and determines who has the highest score.
"""

def get_highest_student(ahmed, mohamed, ali):

    if ahmed > mohamed and ahmed > ali:
        return "Ahmed has the highest degree"

    elif mohamed > ahmed and mohamed > ali:
        return "Mohamed has the highest degree"

    elif ali > ahmed and ali > mohamed:
        return "Ali has the highest degree"

    elif ahmed == mohamed == ali:
        return "All students have the same degree"

    else:
        return "There is a tie between two students"


# Get user input
ahmed_degree = float(input("Enter Ahmed's degree: "))
mohamed_degree = float(input("Enter Mohamed's degree: "))
ali_degree = float(input("Enter Ali's degree: "))

# Get result
result = get_highest_student(ahmed_degree, mohamed_degree, ali_degree)

print(result)



# best practices:

students = {
    "Ahmed": ahmed_degree,
    "Mohamed": mohamed_degree,
    "Ali": ali_degree
}

highest = max(students, key=students.get)

print(f"{highest} has the highest degree")

