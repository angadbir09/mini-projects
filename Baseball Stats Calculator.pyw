#Angadbir Singh
#March 28, 2017
#AngadbirSingh<ansl>.pyw
#Assignment - User Input
#This program will help the userdetemine the performance of a baseball player, based on the variables the user inputs

print "This program will help you detemine a Baseball Player's performance\n" #this program will calculate the batting average and slugging average of a baseball player in a season
player_name = raw_input("Enter the Player's Name\n") #player_name is the variable used for the name of the player
times_at_bat = input("Enter the Number of times the Player has been at Bat\n") #times_at_bat is the variable used for the number of times the player battted
singles = input("Enter the Number of Singles the Player had hit\n") #singles is the variable used for the number of singles the player hit
doubles = input("Enter the Number of Doubles the Player had hit\n") #doubles is the variable used for the number of doubles the player hit
triples = input("Enter the Number of Triples the Player had hit \n") #triples is the variable used for the number of triples the player hit
home_runs = input("Enter the Number of Home Runs the Player had hit\n") #home_runs is the variable used for the number of home runs the player hit
total_hits = singles + doubles + triples + home_runs #total_hits is the variable used for the total number of hits by the player
batting_average = total_hits/times_at_bat #batting_average is the variable used for the batting average of the player and the formula calculates it
slugging_average = (singles + doubles * 2 + triples * 3 + home_runs * 4)/times_at_bat #slugging_average is the variable used for the slugging average of the player and the formula calculates it
print player_name,"'s Batting Average is ",batting_average #tells the user the batting average of the player
print player_name,"'s Slugging Average is ",slugging_average #tells the user the slugging average of the player

#This program will help the user detemine the performance of a baseball pitcher, based on the variables the user inputs

print "\n\nThis program will help you detemine a Baseball Pitcher's performance\n" #this program will calculate the ERA of a baseball pitcher in one game
pitcher_name = raw_input("Enter the Pitcher's Name\n") #pitch_name is the variable used for the name of the pitcher
earned_runs = input("Enter the Number of Earned Run given up by the Pitcher\n") #earned_runs is the variable used for the number of earned run the pitcher gave up
innings_pitched = input("Enter the Number of Inning pitched by the Pitcher\n") #innings_pitched is the variable used for the number of inning the pitcher pitched in the game
innings_in_a_game = input("Enter the Number of Innings in a Game\n") #inning_in_a_game is the variable used for the number of inning in the game
ERA = (earned_runs * innings_in_a_game)/innings_pitched #ERA is the variable used for the overall earned run average of the pitch in a game
print pitcher_name,"'s ERA (Earned Run Average) is", ERA*1.0 #tells the user the ERA of the player
