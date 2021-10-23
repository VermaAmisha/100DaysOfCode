student_scores = input("Input a list of student heights ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
# print(student_scores)

# Find highest score of all
# max() function can also be used to find highest/maximum number of all
# min() function can also be used to find lowest/minimum number of all 

# print(max(student_scores))
# print(min(student_scores))

highest_score = 0
for j in student_scores:
    if j > highest_score:
        highest_score = j


print(f"The highest score in the class is: {highest_score}")
