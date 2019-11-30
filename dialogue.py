#Thomas Standley
#AWAKENING
#Final project
#This file is strictly for the dialouge part of the game. The main game code will have import dialogue. 
#All the variables will be arguments for the display_text function




story_Inter = 'Coming from deep inside your mind you hear a strange voice. Speaking sweet and soft a woman\'s voice says: "Wake up, death is not ready for you... Every decision you make will have an effect. You will take damage and gain health along the way. Wake up...\"'

story_Intro = 'You slowly open your eyes and all you see is a blinding bright light. You try and raise your arm to block it out but the pain is incredible. You slowly turn onto your side and as soon as you move there is a searing sharp pain that runs through the back of your skull. You use your other arm and touch the back of your head, finding it crusted in dried blood. Now laying on your side you open your eyes again and see that the light is coming from a small hole a long ways above you and everything else is covered in darkness. As your eyes adjust more you can tell the walls are rock and you could probably crawl to the nearest one. While deciding what to do a sudden great fear comes over you. You have no idea where you are or how you ended up here. Do you:'

story_CrawlA = 'You slowly crawl while reaching out with your hands to the wall nearest you. Every movement brings unbearable pain. After a few short moments you finally feel the rock surface. As you reach up you find a small ledge that you can grab on to. After some struggle you finally manage to pull yourself to your feet. Looking behind you, you can see the small pinhole of light shining down into a massive cavern. Do you:'

story_CrawlB = 'Slowly you turn your body away from the wall nearest you. With every movement, more agonizing than the last, you crawl for what seems like an eternity. While panting hard, you reach your hand out to pull you along one more time and you feel nothing. You quickly realize the ground is no longer beneath your hands. You can\'t see anything but you reach your hands down and can feel that the rock edge goes straight down. You realize this must be a large crevice in the ground. Do you:'

story_Stand = 'With excruciating pain you roll from your side onto your stomach. You take a few deep breaths to rest for a moment and let some of the blinding pain subside. Slowly you pull your knees under you and sit up. You put one foot in front of you and then push up. Screaming, you stand and slowly bring both feet under you. Instantly you feel dizzy and fall. You don\'t even feel your head smash the ground.'

story_Wall_Right = 'You leave your hand on the wall and turn to your right. You are walking very cautiously in complete darkness with an unbelievable amount of pain. Without warning you run head first into a wall, making the pain blind you for a moment. Do you:'

story_Wall_Left = 'You place your right hand on the wall and slowly turn your body around. Cautiously you follow the wall for several steps. Your steps are slow because of the pain. To your left you pass where the light is hitting the floor to the cavern. You stop to take a breath. Do you:'

story_Wall_Turn_Around = 'After taking a few moments to regain your thoughts you slowly turn your self back around. You follow the wall while keeping your hand up to make sure you don\'t run into anything. You pass the spot you first stood at and keep walking. To your left you pass where the light is hitting the floor to the cavern. You stop to take a breath. Do you:'


story_Wall_Light = 'Breathing hard you are looking at where the light is hitting the cavern floor. Slowly pushing yourself off the wall you take one step, then another. You stand for a moment to catch your balance. With extreme difficulty you put one foot in front of the other, almost falling a few times. Panting you reach the light. Slowly you put your hand in the light, it feels warm. Then you walk fully into the light. You feel your feet leave the ground. Floating you hear the same voice as before: “You are not yet ready”. You then slam back to the ground.'

story_Wall_Follow = 'With your hand on the wall you keep walking. The wall slowly curves towards you. After a few more steps you can see that the wall ends. You take another step and notice you are standing the mouth of a tunnel. The light is directly behind you. Do you:'

story_Stand_Light = 'Breathing hard you are looking at where the light is hitting the cavern floor. You stand for a moment to catch your balance. With extreme difficulty you put one foot in front of the other, almost falling a few times. Panting you reach the light. Slowly you put your hand in the light, it feels warm. Then you put your whole body in the light. You feel your feet leave the ground. Floating you hear the same voice as before: “You are not yet ready”. You then slam back to the ground.'

walk_Stright_question_story = 'You slowly pull yourself back to your feet. Looking sright ahead you can see the out line of what looks like an opening to a tunnel or smaller cave. Do you walk straight ahead? (Y/N)'

walk_Stright_question_story_no = 'You stand there for a few moments to gather your thoughts. You feel the light pull you back in. Once again your feet are off the ground. The voice comes back: "Again young one you are not read." You slammed to the ground again.'

story_Crevice_Right = 'With an extreme effort you back away from the crevice to keep from falling in. With your hands you find the edge. Using your hands to pull yourself to your right you start crawling. Almost immediately your hand hits what feels like a root hanging from the celing. Grasping it with both hands you pull yourself to your feet. Panting, you stand there for a moment to catch your breath. Your eyes have adjusted enough that you can see the edge of the crevice. You also see the light coming through the ceiling and hitting the floor.'
 
story_Crevice_Left = 'Backing up slowly you turn your body. Your eyes are adjusting and you see a few feet in front of you. It looks like there is a large object in front of you so you start crawling towards it. After only a few moments of painful crawling that object you saw becomes clear. It is a wall that has a sort of rope ladder on it. You pull yourself up to your feet screaming the entire time. Do you crawl up the ladder?(Y/N)'

story_Crevice_Left_Ladder = 'You try to climb up the ladder slowly. You hear a snap and the ladder swings over the crevice. You hang on with all your strength but the other rope on the ladder snaps. You are flung into the crevice. There is nothing for you to grab onto and you are falling into the darkness. As the bottom rushes up you fade out.'

story_Crevice_Left_Turn = 'You take a look at the ladder and think it looks unsafe. You turn around, but you move to quickly. You lose your balance and stumble. You try to grab the edge but you slip over the side of the crevice. As you fall you try to grab the sides but you can\'t. The darkness swallows you up, not knowing you smashed into the bottom.'

story_Crevice_Down = 'Peering over the edge your eyes are adjusting enough that you can see the walls of the crevice. You can’t see the bottom or how deep it is but the walls of the crevice look like it can be scaled. You slowly swing your legs around and dangle your body over the edge. You find some foot holds and start to move slowly down. Stopping to catch your breath you feel the wall crumble under your feet. The entire wall breaks apart plunging you into the depths. You don’t even feel your body smash into the crevice floor.'

story_Fall_Crevice = 'After regaining your balance you put your hand back on the wall. You take a few steps before your stomach jumps into your throat. The earth is going up wards as you are falling in the dark abyss. The bottom rushes up to meet you, but you never feel it.'

story_Crevice_Right_Follow = 'After standing for a few moments you notice that you can see the edge of the crevice. You keep walking and the wall turns slightly towards you. You take another step and notice you are standing at the mouth of a tunnel. The light is directly behind you. Do you:'

story_Walk_Stright = 'You stand in the mouth of the tunnel for a few moments. Finally your eyes are adjusting and some features are becoming clear. There is a small statue in the center against the wall. On either side of the statue is openings for two differnt tunnels. As you get close the statue starts to glow through its cracks.'

story_Touch_Statue = 'The statue looks like a young woman wearing a long robe. Holding an owl in her left hand and a sword in the other. Her eyes are covered with a cloth. As you reach your hand out the staue starts glowing brighter. You place your hand on top. A power rushes through you and you see flashes of a giant battle that only last a moment. You step back reeling, but you are not in as much pain as before. Do you:'

story_Tunnel_Right = 'You look both directions and it looks like both tunnels are the same in size. You turn twords the tunnel on the right and start walking. Entering the tunnel you see the walls are covered in torches, lighting your path. After some time the tunnel comes in an abrupt end at antoher statue that looks exactly like the first one. That same voice comes back:"If you take the Holy Light will you use it to empower yourself?(Y/N) '  

story_Tunnel_Left = 'Looking at both tunnels you take a step towards the tunnel on your left. Instantly you see the statue start glowing a deep red. The tunnel is in complete darkness. Slowly taking a few steps an incredible bright light shines a few feet in front of you. You feel the light peirce your body. A shrill voice screams: "You are not worthy of the Holy Light!"'

story_Sword = 'In your right hand you see a beam of light. When the light fades you are holding a blade. The sword looks like it was forged for a God. A sapphire glows with power in the pommel and an owl is engraved on the hilt. You can feel the power rushing through your body. You look forward and all you see is a bright light.'

story_Self_Empower = 'The familar voice screams: "You are incredibly selfish. The Holy Light could be used to change the future and end these horrible times! You are not worthy of the Light"'

story_Empower_People_No = 'In a stern tone you hear the familiar voice: "You don\'t want to empower yourself but yet you won\'t empower the people. A hero must do all things for the benefit of the people. You are not yet ready for the light"'

story_End = 'That soft familiar voice comes back: "You are the hero that the world needs. I know you have many questions and they will be answered in time. For now know that the fate of all life is dependant on how you use the Holy Light. Go forth and don\'t let the darkness take ahold in your heart."'