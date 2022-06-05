# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# #print(type(height))

# if height >= 120:    ##if else only check one condition but with elif you can check as many condition as                                 you like
#   print("You can ride!")
#   age = int(input("What is your age? "))
#   photo = input("Do you want a photo? Y or N " )
#   Y = True
#   N = False
#   if age < 12:
#     if photo == Y:
#       print("You have to pay $8")
#     else:
#       print("You have to pay $5")
    
#   elif age < 18:
#     if photo == Y:
#       print("You have to pay $10")
#     else:
#       print("You have to pay $7")
#     #print("You have to pay $7")
#   else:
#     if photo == Y:
#       print("You have to pay $15")
#     else:
#       print("You have to pay $12")
#     #print("You have to pay $12")  
 
# else:
#   print("You can't ride!")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
#print(type(height))
bill = 0

if height >= 120:    ##if else only check one condition but with elif you can check as many condition as                                 you like
  print("You can ride!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Kids have to pay ${bill}")
  elif age < 18:
    bill = 7
    print("Children have to pay ${bill}")
  else:
    bill = 12
    print("Adult have to pay ${bill}") 
  photo = input("Do you want photo to be taken? Y or N ")
  if photo == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")
  else:
    print(f"Your final bill is ${bill}")
else:
  print("You can't ride!")