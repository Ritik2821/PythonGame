print("\t\t\t SNAKE,WATER ,GUN")
print("You have only 5 chances to win this game")
player=0
comp=0s
chance=0
import random
while(chance<5):
    ch=str(input("\nEnter your choice\nS-snake\nW-water\nG-gun\n"))
    if ch=="S":
        list=["Snake","Water","Gun"]
        compchoice=random.choice(list)
        if compchoice=="Snake":
            print("Computer's Choice: ",compchoice)
            print("The round is a tie!!")
        elif compchoice=="Water":
            print("Computer's choice: ",compchoice)
            print("Snake drank water ,hence you win this round")
            player=player+1
        else:
            print("Computer's choice: ",compchoice)
            print("Snake shot by the gun hence you lost this game")
            comp=comp+1
        print("Your score : ", player, "Computer's score : ", comp)
        chance = chance + 1

    elif ch=="W":
        list = ["Snake", "Water", "Gun"]
        compchoice = random.choice(list)
        if compchoice == "Snake":
            print("Computer's Choice: ", compchoice)
            print("Snake drank water,hence you lost this round ")
            comp = comp + 1
        elif compchoice == "Water":
            print("Computer's choice: ", compchoice)
            print("The round is a tie!!")

        else:
            print("Computer's choice: Gun")
            print("Water will not affect gun ,hence you win this round")
            player = player + 1
        print("Your score : ", player, "Computer's score : ", comp)
        chance = chance + 1
    elif ch=="G":
        list = ["Snake", "Water", "Gun"]
        compchoice = random.choice(list)
        if compchoice == "Snake":
            print("Computer's Choice: ", compchoice)
            print("Snake shot by the gun ,hence you win this round")
            player= player+ 1
        elif compchoice == 'Water':
            print("Computer's choice: ", compchoice)
            print("Water will not affect gun ,hence computer win this round")
            comp=comp+1
        else:
            print("Computer's choice: Gun")
            print("The round is a tie!!")

        print("Your score : ", player, "Computer's score : ", comp)
        chance = chance + 1
    else:
        print("Enter valid choice!!!")
print("Total Player Score : ", player, "Total Computer Score : ", comp)
if player>comp:
    print("You won the game")
elif player<comp:
    print("Computer won the game")
else:
    print("The match TIES!!")



