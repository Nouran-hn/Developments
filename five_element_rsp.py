## HIERARCHY OF THE ELEMENTS
## Shoe, Bug, Cat, Mouse, Cheese

### shoe steps on mouse
### Shoe steps on bug
###
### Bug eats cheese and makes it moldy
### Bug makes cat exhausted from scratching
###
### Cat rips up shoe
### Cat runs after and eats mouse
###
### Mouse steps on bug
### Mouse eats cheese
###
### Cheese makes cat stomach hurt (Lactose intolerant)
### Cheese makes shoe smell bad
##*******************************************************************************

from random import *
print("Welcome to Nourans five object 'Rock-Paper-Scissors' game!")
print("Both you and the computer start with 20 points. If you win, you earn 1 point, but if you lose the computer wins 1 point. Play hard and 'strategically' to see if you are the next 5 object RSP master!")
print("Hope you enjoy!")

#INPUT
tp=int(input("How many times (rounds) would you like to play? "))

#VARIABLES
Cscore=20
Hscore=20
Hwin=0
Cwin=0

elements=["Shoe", "Bug", "Cat", "Mouse", "Cheese"]

#FOR LOOP
for tp in range(1,tp+1):

#INPUT
    PlayersChoice=input("What element do you choose, please choose ? ( (a)Shoe (b)Bug (c)Cat (d)Mouse (e)Cheese) ")
    print()
    
    while PlayersChoice not in ["A", "B", "C", "D", "E","a", "b", "c", "d", "e"]:
        print("This is not a valid response, please choose from the letters below")
        PlayersChoice=input("What element do you choose, please choose ? ( (a)Shoe (b)Bug (c)Cat (d)Mouse (e)Cheese) ")
        print()

    Compchoice = choice(elements)
    print("Computers Move is", Compchoice)

    print()

#IF STATEMENTS
    if Compchoice == "Shoe":
        if PlayersChoice in ["c","d","C","D"]:
            Hscore = Hscore+1
            Hwin = Hwin +1
            print("You won this round")
            print("You have", Hscore, "points!")
            print()
        else:
            Cscore = Cscore+1
            Cwin = Cwin + 1
            print("Sorry you lost this round")
            print("The computer has", Cscore, "points")
            print()

    elif Compchoice == "Bug":
        if PlayersChoice in ["a","c","C","A"]:
            Hscore = Hscore+1
            Hwin = Hwin +1
            print("You won this round")
            print("You have", Hscore, "points!")
            print()
        else:
            Cscore = Cscore+1
            Cwin = Cwin + 1
            print("Sorry you lost this round")
            print("The computer has", Cscore, "points")
            print()

    elif Compchoice == "Cat":
        if PlayersChoice in ["e","b","E","B"]:
            Hscore = Hscore+1
            Hwin = Hwin +1
            print("You won this round")
            print("You have", Hscore, "points!")
            print()
        else:
            Cscore = Cscore+1
            Cwin = Cwin + 1
            print("Sorry you lost this round")
            print("The computer has", Cscore, "points")
            print()
        
    elif Compchoice == "Mouse":
        if PlayersChoice in ["A","C","a","c"]:
            Hscore = Hscore+1
            Hwin = Hwin +1
            print("You won this round")
            print("You have", Hscore, "points!")
            print()
        else:
            Cscore = Cscore+1
            Cwin = Cwin + 1
            print("Sorry you lost this round")
            print("The computer has", Cscore, "points")
            print()

    elif Compchoice == "Cheese":
        if PlayersChoice in ["B","D","b","d"]:
            Hscore = Hscore+1
            Hwin = Hwin +1
            print("You won this round")
            print("You have", Hscore, "points!")
            print()
        else:
            Cscore = Cscore+1
            Cwin = Cwin + 1
            print("Sorry you lost this round")
            print("The computer has", Cscore, "points")
            print()
print("*"*20)
#TOTALS
print("The total number of points for you is", Hscore)
print("The total number of points for the computer is", Cscore)
print()

print("The number of wins you go is", Hwin)
print("The number of wins the computer got is", Cwin)
print()
print("But this games is based on the number of points you earned so...")
print()

if Hscore == Cscore:
    print("It's a Draw")
    print("Play again to win")
    print()
elif Hscore > Cscore:
    print("You Win with", Hscore, "points!")
    print()
else:
    print("Sorry you Lose")
    print("Play again to win")
    print()
print("*"*20)

#CONCLUSION
print("Thank you for using Nourans five object 'Rock-Paper-Scissors' game!")
print("I hope you had lots of fun!")








