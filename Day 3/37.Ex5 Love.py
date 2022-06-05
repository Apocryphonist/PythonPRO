# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
name = name.lower()
# print(name)
# print(type(name))

countT = name.count("t")
countR = name.count("r")
countU = name.count("u") 
countE = name.count("e") 
 
countL = name.count("l")
countO = name.count("o") 
countV = name.count("v") 
countE = name.count("e") 

countTrue = countT + countR + countU + countE
countLove = countL + countO + countV + countE

finalCount = str(countTrue) + str(countLove)
finalCount =int(finalCount)

if finalCount < 10 or finalCount > 90:
    print(f"Your score is {finalCount}, you go together like coke and mentos.")
elif finalCount >= 40 and finalCount <=50:
    print(f"Your score is {finalCount}, you are alright together.")
else:
    print(f"Your score is {finalCount}.")    
