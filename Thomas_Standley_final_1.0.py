#INF360 -  Programming in Python
#Thomas Standley
#Final Project 
#AWAKENING

#This program is a text adventure game about a person waking up and not knowing where they are or how they got there. 
#The player wakes up and is hurt all ready. The player must make choices to reach the "end". This is not easy. 
# The player will take damage and/or gain health. The idea behind this game is to serve as a prologue to a very large open world RPG that is currently living in my mind. 
#I have an idea that at the end of this prolouge the player will have a memory flashback where the palyer will input their name and chose a class. 

#To do list: 



import random
import time
import dialogue
import aw_func


#This variable to set the health to 10. As the player goes through the game this number can increase and decrease. 
health = 10

#the two lists are to put in all the options how a player may answer the yes or no questions at the end to replay.
yes = ["Y", "y", "yes", "Yes", "YES"]
no = ["N", "n", "no", "No", "NO"]

#This variable is to set the console width so the text only appears so wide in the user's console. 
console_width = 60

#The title function starts the program but is not included in the loop because it really only needs to run once. 
aw_func.title()

#This loop will keep the game code running as long as the players health is above 0.	
while health > 0: 
	aw_func.interlude()

#If the player's health gets to 0 then the loop runs the else. This will ask the player if they would like to play again. If yes it will start the loop over and if no the program will end. 	
else: 
	print('')
	print('-' * console_width)
	choice = input('Death is trying to pull you in. Keep fighting back?(Y/N)')
	print('')
	if choice in yes:
		aw_func.interlude()
	elif choice in no:
		input('Enter to exit')