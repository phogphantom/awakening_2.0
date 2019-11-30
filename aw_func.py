import random
import time
import textwrap
import dialogue
import sys

#This file contains all the fuctions for the game. When the loop starts in the main game code then it starts pulling all the functions from this file. I created this file not only for the oop requirement but to help clean up the code.

#This variable tells the fucntions the size of the console. 
console_width = 60

#The lists that follow are to allow the palyer the some freedom on answering the questions. It helps becuase not all players will answer in the exact same manner.
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes", "YES"]
no = ["N", "n", "no", "No", "NO"]

required = ('Use only A, B, or C. Not case sesitive')
required_2 = ('Answer yes or no')




#This is the starting amount of health for the player.
health = 10 



#This is the title of the game. This function happens outside the loop and will only be called once no matter how many times a player replays the game. 
def title(): 
	title = 'AWAKENING'
	title_centered = title.center(60)
	print('-'*console_width)
	print(title_centered)
	print('-'*console_width)
	controls = 'All choices will be A,B,C or Y/N. (Not case sensitive)'
	print('''
	
	
	''')
	display_text(controls)
	print('''
	
	
	''')
	

#I can not claim this function in whole. This is courtsey of reddit user 'bull_fiddle_blues'. 
# I had the idea of this fucntion and made a seperate file to test something like this. 
# Reddit is a lifesaver.
# This fuction makes all the text apper as if it is being typed out to the console. 
def display_text(text):
    print('-' * console_width)
    i = 0
    for w in text.split():
        i += 1
        if len(w) + i > 60:
            print()
            sys.stdout.flush()
            i = 0
        for c in w:
            print (c,end=''),
            sys.stdout.flush()
            time.sleep(0.09) 
            i += 1
        print (' ',end='')
        sys.stdout.flush()
    print()
    print('-'* console_width)

#This function adds health to the player.	
def addHealth(): 
	global health
	x = random.randint(1,10)
	health += x
	health_added = 'You gained ' + str(int(x)) + ' points of health.'
	current_health = 'Current health:' + str(int(health))
	print('')
	display_text(health_added)
	print('')
	display_text(current_health)


#subtracts health to player, 'taking damage'	
def loseHealth(): 
	time.sleep(1)
	global health
	x = random.randint(1,9)
	health -= x
	health_lost = 'You took ' + str(int(x)) + ' points of damage.'
	health_zero = 'You have died.\nThe darkness is grasping you.'
	current_health = 'Current health:' + str(int(health))
	print('')
	display_text(health_lost)
	print('')
	display_text(current_health)
	if health <= 0:
		display_text(health_zero)

#causes instant death. 
#ends the loop and asks the player to play again. 	
def instaDeath(): 
	global health
	health = 0
	death = 'The sweet voice says: "You have made poor choices". \n You have died'
	display_text(death)


#This is the start. If the player dies and wants to play again it will start here.
def interlude(): 
	
	display_text(dialogue.story_Inter)
	
	time.sleep(.25)
	print('')
	global health
	health = 10
	choice = input('Wake up?(Y/N)')
	if choice in yes:
		intro()
	elif choice in no:
		print('We will be waiting')
	else:
		print(required_2)
		interlude()

#This function contains the players first choice. other than the yes or no of the interlude function
def intro():
	current_health = 'Current health:' + str(int(health)) 
	print('')
	
	display_text(dialogue.story_Intro)
	time.sleep(.25)
	print('')
	display_text(current_health)
	print('')
	print('''
A. Crawl to the wall and try to stand
B. Crawl in the opposite direction
C. Try to stand where you are''')
	choice = input('>>> ') 
	if choice in answer_A:
		crawl_A()
	elif choice in answer_B:
		crawl_B()
	elif choice in answer_C:
		stand()
	else:
		print(required)
		intro()

#player crawls to wall to stand
def crawl_A():
	current_health = 'Current health:' + str(int(health)) 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_CrawlA)
	time.sleep(.25)
	print('')
	display_text(current_health)
	print('')
	print('''
A. Follow the wall to the right
B. Follow the wall to the left
C. Try to walk towards the light''')
	choice = input('>>>')
	if choice in answer_A:
		wallRight()
	elif choice in answer_B:
		wallLeft()
	elif choice in answer_C:
		wallLight()
	else:
		print(required)
		crawl_A()

#player crawls and finds crevice
def crawl_B(): 
	current_health = 'Current health:' + str(int(health))
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_CrawlB)
	time.sleep(.25)
	print('')
	display_text(current_health)
	print('')
	print('''
A. Follow the crevice to your right.
B. Follow the crevice to your left.
C. Try to climb down the crevice.''')
	choice = input('>>>')
	if choice in answer_A:
		creviceRight()
	elif choice in answer_B:
		creviceLeft()
	elif choice in answer_C:
		creviceDown()
	else:
		print(required)
		crawl_B()

#stands where the player is, first time taking damage
def stand(): 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Stand)
	time.sleep(1)
	print('')
	loseHealth()
	
	if health > 0:
		print('''
A. Crawl to the wall.
B. Try to stand again and walk towards the light.''')
		choice = input('>>>')
		if choice in answer_A:
			crawl_A()
		elif choice in answer_B:
			standLight() 

#player goes right along the wall
def wallRight(): 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Wall_Right)
	time.sleep(.25)
	print('')
	loseHealth()
	if health > 0:
		print('''
A. Turn around
B. Walk away from the wall''')
		choice = input('>>>')
		if choice in answer_A:
			wallTurn()
		elif choice in answer_B:
			display_text(dialogue.story_Fall_Crevice) 
			instaDeath()
			time.sleep(2)
			print('''
				
				
				''')
	
#player goes left along the wall
def wallLeft():
	current_health = 'Current health:' + str(int(health)) 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Wall_Left)
	print('')
	display_text(current_health)
	time.sleep(.25)
	print('')
	print('''
A. Keep following the wall
B. Walk to the light''')
	choice = input('>>>')
	if choice in answer_A:
		wallFollow()
	elif choice in answer_B:
		wallLight()


#player walks to light after standing
def wallLight(): 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Wall_Light)
	time.sleep(.25)
	loseHealth()
	if health > 0: 
		display_text(dialogue.walk_Stright_question_story)
		choice = input('>>>')
		if choice in yes:
			walkStright()
		elif choice in no:
			display_text(dialogue.walk_Stright_question_story_no)
			instaDeath()
			time.sleep(2)
			print('''
				
				
				''')
			
#turns around after hitting head		
def wallTurn(): 
	current_health = 'Current health:' + str(int(health))
	print('')
	
	display_text(dialogue.story_Wall_Turn_Around)
	time.sleep(.25)
	print('')
	print('')
	display_text(current_health)
	print('')
	print('''
A. Keep following the wall
B. Walk to the light''')
	choice = input('>>>')
	if choice in answer_A:
		wallFollow()
	elif choice in answer_B:
		wallLight()

#keepings following wall, ends in first tunnel	
def wallFollow():
	current_health = 'Current health:' + str(int(health)) 
	print('')
	
	display_text(dialogue.story_Wall_Follow)
	time.sleep(.25)
	print('')
	print('')
	display_text(current_health)
	print('')
	print('''
A. Walk stright into the tunnel
B. Walk towards the light
		''')
	choice = input('>>>')
	if choice in answer_A:
		walkStright()
	elif choice in answer_B:
		wallLight()

#stands after finding root	
def creviceRight(): 
	current_health = 'Current health:' + str(int(health))
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Crevice_Right)
	print('')
	display_text(current_health)
	print('')
	print('''
A. Keep following the crevice
B. Walk towards the light''')
	choice = input('>>>')
	if choice in answer_A:
		creviceRightFollow()
	elif choice in answer_B:
		standLight()

#ends in first tunnel
def creviceRightFollow(): 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Crevice_Right_Follow)
	print('')
	print('''
A. Walk sright
B. Walk to the light''')
	choice = input('>>>')
	if choice in answer_A:
		walkStright()
	elif choice in answer_B:
		standLight()

#player finds ladder, falls to death	
def creviceLeft(): 
	current_health = 'Current health:' + str(int(health))
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Crevice_Left)
	time.sleep(.25)
	print('')
	display_text(current_health)
	print('')
	choice = input('>>>')
	if choice in yes:
		print('')
		display_text(dialogue.story_Crevice_Left_Ladder)
		instaDeath()
		time.sleep(5)
		print('''
			
			
			''')
	elif choice in no:
		print('')
		display_text(dialogue.story_Crevice_Left_Turn)
		instaDeath()
		time.sleep(5)
		print('''
			
			
			''')
			
#try to climb down crevice, causes death				
def creviceDown(): 
	print('')
	
	time.sleep(.15)
	display_text(dialogue.story_Crevice_Down)
	instaDeath()
	time.sleep(5)
	print('''
		
		
		''')
		
#walks into tunnel		
def walkStright():  
	current_health = 'Current health:' + str(int(health))
	print('')
	
	display_text(dialogue.story_Walk_Stright)
	time.sleep(.15)
	print('')
	display_text(current_health)
	print('')
	print('Touch the statue?(Y/N)')
	choice = input('>>>')
	if choice in yes:
		display_text(dialogue.story_Touch_Statue)
		addHealth()
		print('''
A. Go in the tunnel on your right
B. Go in the tunnel on your left''')
		choice = input('>>>')
		if choice in answer_A:
			tunnelRight()
		elif choice in answer_B:
			tunnelLeft()
	elif choice in no:
		print('''
A. Go in the tunnel on your right
B. Go in the tunnel on your left''')
		choice = input('>>>')
		if choice in answer_A:
			tunnelRight()
		elif choice in answer_B:
			tunnelLeft()

#This is the tunnel that is the endgame, player will finish game if answering the questions correctly. 
def tunnelRight(): 
	print('')
	
	display_text(dialogue.story_Tunnel_Right)
	time.sleep(.15)
	choice = input('>>>')
	if choice in yes:
		print('')
		display_text(dialogue.story_Self_Empower)
		print('''
			
			
		''')
		time.sleep(3)
		instaDeath()
			
	elif choice in no:
		print('Will you use the Holy Light is empower the people?(Y/N)')
		choice = input('>>>')
		if choice in yes:
			display_text(dialogue.story_Sword)
			time.sleep(3)
			end()
		elif choice in no:
			print('')
			display_text(dialogue.story_Empower_People_No)
			print('''
			
			
			''')
			time.sleep(3)
			instaDeath()
				
#goes down left tunnel, causes death			
def tunnelLeft(): 
	print('')
	
	display_text(dialogue.story_Tunnel_Left)
	instaDeath()
	print('''
		
		
	''')
	time.sleep(3)

#walk into light, take damage. 		
def standLight(): 
	print('')
	
	display_text(dialogue.story_Stand_Light)
	time.sleep(.15)
	print('')
	loseHealth()
	if health > 0: 
		display_text(dialogue.walk_Stright_question_story)
		choice = input('>>>')
		if choice in yes:
			walkStright()
		if choice in no:
			display_text(dialogue.walk_Stright_question_story_no)
			instaDeath()
			time.sleep(2)
			print('''
				
				
			''')
	elif health <= 0:
		print('')

#This is the end of the current game. Sets up what might be to come
def end(): 
	print('')
	
	print('')
	display_text(dialogue.story_End)
	time.sleep(3)
	print('''
		
		
	''')
	input('Go forth')
	
