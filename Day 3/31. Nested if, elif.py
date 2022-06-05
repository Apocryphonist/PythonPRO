print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
#print(type(height))

if height >= 120:    ##if else only check one condition but with elif you can check as many condition as                                 you like
  print("You can ride!")
  age = int(input("What is your age? "))
  if age < 12:
    print("You have to pay $5")
  elif age <=18:
    print("You have to pay $12")
  else: 
    print("You have to pay $18")
else:
  print("You can't ride!")