print("Hello and welcome to Nouran's snowball game!")
inst=input("Would you like to see the instructions for the game? (y/n)")
if inst in ["Yes","yes","y","Y","YES"]:
    print("Imagine this... You are playing with your friend and you decided to have a major snowball fight. If you win that means you are the master, but be careful with your decisions.")
    print("The way to play is simple. You will have ten rounds, trying to dodge snowballs from the computer. You will have five moves to choose from so that you can hide from the icy snow coming your way. All you have to do is put in different letters that will move you. You can move up, down, left, right or you can stay where you are. If you don't make a move in 4 seconds you automatically lose that round. Starting from having the score of 20 points, lets see if you can rise up or if you will fall into the snowbank.")
    print("Goodluck!")

print()
print("*"*20)
print()

from random import *
from time import *
#VARIABLES
moves=["Up","Down","Right","Left","Stay"]
score=20

#FOR LOOP
for x in range(1,11):
  
#INPUT
    begin=input("Would you like to begin this round? (y/n)")
    if begin in ["Yes","yes","y","Y","YES"]:
      
      print()
      Compchoice = choice(moves)
      print("Computers Move is", Compchoice)
      print()
        
      timeStart = time()
        
      PlayersChoice=input("What move do you choose? Please choose from the following ( U) Up, D) Down, R) Right ,L) Left, S) Stay ) ")
      
      timeFinish = time()
      
      totalTimeToAnswer = timeFinish - timeStart
      
      print()
        
      while PlayersChoice not in ["U","D","R","L","S","u","d","r","l","s",]:
          print("This is not a valid response, please choose from the letters below")
          PlayersChoice=input("What move do you choose? Please choose from the following ( U) Up, D) Down, R) Right ,L) Left, S) Stay ) ")
          print()
  
    
  #IF STATEMENTS
      if Compchoice == "Up":
          if totalTimeToAnswer <= 4:
            if PlayersChoice in ["U","u"]:
                  score = score-7
                  print("Sorry you lost this round")
                  print("You have", score, "points!")
                  print("-"*20)
            else:
                  score = score + 5
                  print("You won this round")
                  print("You have", score, "points!")
                  print("-"*20)
          else:
            print("Sorry you lost because you took too much time")
            score = score-7
            print("You have", score, "points!")
            print("-"*20)
            
      if Compchoice == "Down":
          if totalTimeToAnswer <= 4:
            if PlayersChoice in ["D","d"]:
                  score = score-7
                  print("Sorry you lost this round")
                  print("You have", score, "points!")
                  print("-"*20)
            else:
                  score = score + 5
                  print("You won this round")
                  print("You have", score, "points!")
                  print("-"*20)
          else:
            print("Sorry you lost because you took too much time")
            score = score-7
            print("You have", score, "points!")
            print("-"*20)
       
      if Compchoice == "Left":
          if totalTimeToAnswer <= 4:
            if PlayersChoice in ["L","l"]:
                  score = score-7
                  print("Sorry you lost this round")
                  print("You have", score, "points!")
                  print("-"*20)
            else:
                  score = score + 5
                  print("You won this round")
                  print("You have", score, "points!")
                  print("-"*20)
          else:
            print("Sorry you lost because you took too much time")
            score = score-7
            print("You have", score, "points!")
            print("-"*20)
       
      if Compchoice == "Right":
        if totalTimeToAnswer <= 4:
          if PlayersChoice in ["R","r"]:
                  score = score-7
                  print("Sorry you lost this round")
                  print("You have", score, "points!")
                  print("-"*20)
          else:
                  score = score + 5
                  print("You won this round")
                  print("You have", score, "points!")
                  print("-"*20)
        else:
            print("Sorry you lost because you took too much time")
            score = score-7
            print("You have", score, "points!")
            print("-"*20)
    
      if Compchoice == "Stay":
          if totalTimeToAnswer <= 4:
            if PlayersChoice in ["S","s"]:
                  score = score-7
                  print("Sorry you lost this round")
                  print("You have", score, "points!")
                  print("-"*20)
            else:
                  score = score + 5
                  print("You won this round")
                  print("You have", score, "points!")
                  print("-"*20)
          else:
            print("Sorry you lost because you took too much time")
            score = score-7
            print("You have", score, "points!")
            print("-"*20)
  
  
print("*"*20)
#TOTALS
print("Your total number of points is", score)
print()
  
if score >= 5:
    print("You won 5 or more times so you Win with", score, "points!")
    print()
else:
    print("You couldn't win 5 or more rounds so I am sorry, but you lost.")
    print("Play again to win")
    print()
print("*"*20)
  
#CONCLUSION
print("Thank you for using Nourans snowball tourney game!")
print("I hope you had lots of fun!")
playAgain=input("Would you like to play again? (Y/N)")

while playAgain in ["y","Y","yes","Yes","YES"]:
  continue
else:
  print("Okay hope to see you again!")


