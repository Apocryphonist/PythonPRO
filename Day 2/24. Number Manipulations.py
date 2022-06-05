##rounding up to two decimals places 

print(int(8/3))

print(round(8 / 3, 2))
print(round(2.6666666, 2))

##if you use two // instead of one / you will get integer number instead of floating number

print(9/3)
print(9//3)

###if you are trying to add numbers with someones score instead of adding +1 or taking away -1 you can do this

score = 0
score -= 1
print(score)  
score +=2
print(score)
##you can even do divide and multiply using the same method

score *= 9
print(score)
score //=3  ##// to get integer number 
print(score)

#print('Your score is ' + score)  ##this will give you type error coz you are trying to add string with interger and boolean,  so you can use F strings 

score = 0
height = 1.8
isWinning = True

print(f"my score is {score}, my height is {height}, and I am {isWinning}")
