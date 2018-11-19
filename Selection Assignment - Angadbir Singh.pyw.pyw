#Angadbir Singh
#April 24, 2017
#Selection Assignment - Angadbir Singh.pyw
#Rock, Paper, Scissors, Lizzard, and Spock will be the choices given to the users, and their choice of hand shape will be simulated against the computer and give the results

player=raw_input("Enter your Hand-Shape:\n")#the user picks a hand-shape and types it up making sure the first letter is upper case
import random
computer=random.randrange(5)+1 #the computer randomly selects a number from 1 to 5
if computer==1: #and each of the numbers get assigned a hand-shape, so making the computer randomly select a hand-shape
    computer="scissors" #1 becomes Scissors
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie" #if both user and the computer pick the same hand shape the program will output a TIE
    elif player=="paper": #a group of elifs get nested inside the if and the elifs to do detemine the output for each of the options
        print "Computer's Hand-Shape: \n", computer #depending on if the user inputed a valid response the programs will check to see the relation between the two inputs, wheither ones beats the other, or if its  tie 
        print "You Lose", computer, "cuts", player
    elif player=="rock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "crushes", computer
    elif player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "decapitates", player
    elif player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "smashes", computer
    else:
        print "INVAID SELECTION" #if none of the valid selections are picked the computer will let the user know
elif computer==2:
    computer="paper"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="scissors":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "cuts", computer
    elif player=="rock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "covers", player
    elif player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "eats", computer
    elif player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "disproves", player
    else:
        print "INVAID SELECTION"
elif computer==3:
    computer="rock"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="paper":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "covers", computer
    elif player=="scissors":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "crushes", player
    elif player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "crushes", player
    elif player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "vapourises", computer
    else:
        print "INVAID SELECTION"
elif computer==4:
    computer="lizard"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="paper":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "eats", player
    elif player=="scissors":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "decapitates", computer
    elif player=="rock":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "crushes", computer
    elif player=="spock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "poisons", player
    else:
        print "INVAID SELECTION"
elif computer==5:
    computer="spock"
    if player==computer:
        print "Computer's Hand-Shape: \n", computer
        print "Tie"
    elif player=="paper":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "disproves", computer
    elif player=="scissors":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "smashes", player
    elif player=="rock":
        print "Computer's Hand-Shape: \n", computer
        print "You Lose", computer, "vapourises", player
    elif player=="lizard":
        print "Computer's Hand-Shape: \n", computer
        print "You Win", player, "poisons", computer
    else:
        print "INVAID SELECTION"
