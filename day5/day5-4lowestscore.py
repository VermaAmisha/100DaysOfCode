student_scores = input("Input a list of student heights ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
# print(student_scores)

# Find lowest score of all
# max() function can also be used to find highest/maximum number of all
# min() function can also be used to find lowest/minimum number of all 

# print(max(student_scores))
# print(min(student_scores))

lowest_score = 100
for j in student_scores:
    if j < lowest_score:
        lowest_score = j


print(f"The lowest score in the class is: {lowest_score}")
