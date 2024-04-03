import random
import math
#asking the user to give the highest and lowest number of the range
lower_bound=int(input("Enter the lowest number of the range: "))
upper_bound=int(input("Enter the highest number of the range: "))
#create a list with all the possible number
lower_upper_bound_list=list(range(lower_bound,upper_bound+1))
print("The following numbers can be the guess: "+" "+ str(lower_upper_bound_list))
#generates a random number and keeps it in a variable

x=random.randint(lower_bound, upper_bound)
#Minimum number of guessing = log2(Upper bound – lower bound + 1)
min_num_guessing=round(math.log(upper_bound-lower_bound+1))
print("You have" + " "+ str(min_num_guessing) + " "+"possibilities to guess the number")
#while for repetitive guessing
count=0
n=0
while count<min_num_guessing:
    print("You used " + " "+ str(count)+" "+ "guesses, you have" + " "+ str(min_num_guessing-n)+" "+"left")
    count+=1
    n+=1
    guess=int(input("Your"+" " +str(count) +" "+"guess: "))
    #message for the quess
    if guess == x:
        print("Congratulation! You guessed the number")
        break
    elif guess > x:
        print("The number is too high")
    else:
        print("The number is too small")
#message for the counts
if count<min_num_guessing:
     print("Congratulation! You guessed in" + " "+str(count)+" "+"number of guesses" )
else:
     print("Better luck next time. The number is" +" "+str(x))



