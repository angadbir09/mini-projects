#Angadbir Singh
#April 24, 2017
#Selection Assignment - Angadbir Singh.pyw
#Rock, Paper, Scissors, Lizzard, and Spock will be the choices given to the users, and their choice of hand shape will be simulated against the computer and give the results
#this program shorter version of the program as it will not display how the user wins/loses due to the atempt of limiting the amount of ifs and elifs being used 

player=raw_input("Enter your Hand-Shape:\n")#the user picks a hand-shape and types it up making sure the first letter is upper case
import random
computer=random.randrange(5)+1 #the computer randomly selects a number from 1 to 5
if computer==1: #and each of the numbers get assigned a hand-shape, so making the computer randomly select a hand-shape
    computer="scissors" #1 becomes Scissors
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie" #if both user and the computer pick the same hand shape the program will output a TIE
    elif player=="paper" or player=="lizard": #a group of elifs get nested inside the if and the elifs to do detemine the output for each of the options
        print "Computer's Hand-Shape: \n", computer #depending on if the user inputed a valid response the programs will check to see the relation between the two inputs, wheither ones beats the other, or if its  tie 
        print "You Lose"
    elif player=="rock" or player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win"
    else:
        print "INVAID SELECTION" #if none of the valid selections are picked the computer will let the user know
        
elif computer==2:
    computer="paper"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="scissors" or player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Win"
    elif player=="rock" or player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose"
    else:
        print "INVAID SELECTION"
elif computer==3:
    computer="rock"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="paper" or player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win"
    elif player=="scissors" or player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose"
    else:
        print "INVAID SELECTION"
elif computer==4:
    computer="lizard"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="paper" or player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose"
    elif player=="scissors" or player=="rock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win"
    else:
        print "INVAID SELECTION"
elif computer==5:
    computer="spock"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="paper" or player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Win"
    elif player=="scissors" or player=="rock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose"
    else:
        print "INVAID SELECTION"

