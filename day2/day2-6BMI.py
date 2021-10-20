# BMI = Body Mass Index - calculates the body weight as per the height- whether the person is under/overweighed or has right weight

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")

BMI = float(weight) / float(height) ** 2
print(BMI)
