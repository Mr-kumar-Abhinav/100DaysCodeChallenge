# print("Calculating average height of students in a class")

# student_heights = input("enter the list of heights of students: ").split()

# for i in range(0, len(student_heights)):
#     student_heights[i] = int(student_heights[i])
# print(student_heights)


# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)


# total_count = 0
# for count in student_heights:
#     total_count += 1
# print(total_count)

# avg_height = total_height / total_count
# print(round(avg_height))


# # Finding the maximum marks of student
# student_marks = input("enter the list of marks of students: ").split()

# for i in range(0, len(student_marks)):
#     student_marks[i] = int(student_marks[i])
# print(student_marks)


# max_marks = 0
# for mark in student_marks:
#     if mark > max_marks:
#         max_marks = mark

# print(max_marks)


# # finding sun of evens btwn 1-100.
# total_sum = 0
# for i in range(2,101,2):
#     total_sum = total_sum + i

# print(total_sum)


# fizzbuzz game

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)


#  