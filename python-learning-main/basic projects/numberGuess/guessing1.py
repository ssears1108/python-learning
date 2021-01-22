import random
import math

#intro user interactions stuff
print("Hello Gamer Lets Play the Number Guessing Game!")
print("Let us start by choosing our range of numbers to guess from\n")

#getting inputs
lower=int(input("Enter Lower Bound: "))
upper=int(input("Enter Upper Bound: "))

#creating the random number the user will have to guess
x= random.randint(lower, upper)
print("\n\tYou have only ", round(math.log(upper-lower +1, 2)), " chances to guess the interger!\n")

#initilizing guesses
count = 0

#the guessing code stuff
while count < math.log(upper - lower +1, 2):
    count +=1

    guess=int(input("Guess an number: "))

    if x == guess:
        print("Congratulations you did it in ", count, " try")
        break
    elif x>guess:
        print("You guessed to small")
    elif x< guess:
        print("You guessed to high")

if count >= math.log(upper - lower +1, 2):
    print("\nThe number is %d"%x)
    print("\tBetter luck next time")
