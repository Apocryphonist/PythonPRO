# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#print(type(height))  #to find out type of variables


#Write your code below this line 👇
## BMI = (weight(kg)/Height^2(m^2))
height = float(height)
weight = float(weight)
BMI = (int(weight / height ** 2))
print(BMI)


# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# weight_as_int = int(weight)
# height_as_float = float(height)

# # Using the exponent operator **
# bmi = weight_as_int / height_as_float ** 2
# # or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)

# bmi_as_int = int(bmi)

# print(bmi_as_int)