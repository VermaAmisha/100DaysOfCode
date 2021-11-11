# Debug the following code:

# student_heights = input("Input a list of student heights ").split()
# for i in range(0, len(student_heights)):
#     student_heights[i] = int(student_heights[i])

# total_height = 0
# for j in student_heights:
# total_height += j     # after for loop there should be an indentation

# total_students = 0
# for k in student_heights:
# total_students += 1    # after for loop there should be an indentation

# average_height = total_height / total_students
# print(average_height)


student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

total_height = 0
for j in student_heights:
    total_height += j

total_students = 0
for k in student_heights:
    total_students += 1

average_height = total_height / total_students
print(average_height)
# after for loop there should be an indentation
