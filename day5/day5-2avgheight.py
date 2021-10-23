student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
# print(student_heights)

# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)

# all the avove can also be done but it does not include for loop so it is commented out

total_height = 0
for j in student_heights:
    total_height += j
  # print(total_height)

total_students = 0
for k in student_heights:
    total_students += 1
  # print(total_students)

average_height = total_height / total_students
print(average_height)
