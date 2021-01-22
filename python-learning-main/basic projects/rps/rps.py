import random
import math

#rock crush scissors
#scissors cut paper
#paper covers rock
#lizard poisions spock
#spock lazers rock
#scissors decapites lizard
#paper disproves spock
#lizzard eats paper
#rock crushes lizard
#spock smashes scissors


def rpsSwitch(argument):
    switcher ={
        1:  "Rock",
        2: "Paper",
        3: "Scissors",
        4: "Lizzard", 
        5: "Spock"
    }
    print(switcher.get(argument, "invalid answer"))

def winnerCheck(user, ai):
    if user == ai:
        print("We tied")
    elif user == 1:
        if ai == 2:
            print("Paper cover Rock, You Loose")
        elif ai ==3:
            print("Rock Smashes Scissor, You Win")
        elif ai == 4:
            print("Rock Kills Lizard, You Win")
        elif ai == 5:
            print("Spock Vaporizes Rock, You Loose")
    elif user == 2:
        if ai == 1:
            print("Paper cover Rock, You Loose")
        elif ai == 3:
            print("Scissors cuts Paper, You Loose")
        elif ai == 4:
            print("Lizzard eats Paper, You Loose")
        elif ai == 5:
            print("Paper disproves Spock, You Win")
    elif user == 3:
        if ai == 1:
            print("Rock Smashes Scissor, You Loose")
        elif ai == 2:
            print("Scissors cuts Paper, You Win")
        elif ai == 4:
            print("Scissors dicapitates Lizzard, You Win")
        elif ai == 5:
            print("Spock breaks Scissors, You Loose")
    elif user == 4:
        if ai == 1:
            print("Rock Kills Lizard, You Loose")
        elif ai == 2:
            print("Lizzard eats Paper, You Win")
        elif ai == 3:
            print("Scissors dicapitates Lizzard, You Loose")
        elif ai == 5:
            print("Lizard poisons Spock, You Win")
    elif user == 5:
        if ai == 1:
            print("Spock Vaporizes Rock, You Win")
        elif ai == 2:
            print("Papper disproves Spock, You Loose")
        elif ai == 3:
            print("Spock breaks Scissors, You Win")
        elif ai == 4: 
            print("Lizzard poisons Spock, You Loose")   



yn = 0
rock = 1
paper =2
scissors=3
lizard=4
spock=5



print("Let's PLay Rock Paper Scissors Lizard Spock!\n")
while (yn == 0):
    choice = random.randint(1, 5)
    print("Select Your Choice")
    print("Type:\n1 for rock\n2 for scissors\n3 forpaper\n4 for lizzard\n5 for spock\n")
    x = int(input("Enter your choice: "))
    print("Your choice: ")
    rpsSwitch(x)
    print("")
    print ("My Choice: ")
    rpsSwitch(choice)
    print("")
    winnerCheck(x, choice)
    yn = int(input("Play again?\n type 0 for yes, 1 for no\n"))


