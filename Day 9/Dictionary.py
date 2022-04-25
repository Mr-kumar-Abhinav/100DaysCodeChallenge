programming_dict = {
    "key": "value",
    "key2": "value2",
    "key3": "value3"
}

# accessing a dict. element:

# print(programming_dict["key2"])

# adding new element to dictionary
programming_dict["name"] = "kumar abhinav"
programming_dict["name"] = "kumar abhinav anshu"

# loop through a dictionary
for key in programming_dict:
    print(programming_dict[key])


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "good"
    elif score > 70:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "fail"

print(student_grades)


# Nesting

dict_dictionaries = {
    "france": "paris",
    "USA": "DC"
}

dict_lists = {
    "indian_cities": {"cities_visited": ["Delhi", "kolkata", "Mumbai"]}
}  # A list in a dictionary of cities_visitd in a dictionary named indian_cities. this is nesting.


order = {
    "starter": {
        1: "salad",
        2: "soup"},
    "main": {
        1: ["burger", "fries"],
        2: ["steak"]},
    "dessert": {
        1: ["ice cream"],
        2: []}
}

print(order["main"][2][0])