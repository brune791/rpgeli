from story_func import character_Creation
from story_func import story_Two_Questions_Base
from story_func import storyline_preset_V2
from story_func import Room

def chapter_One():
    #character_Creation()

    """ story_Two_Questions_Base("you wake up and find your self in a dimly lit room","as you stand up and look around you see a big metal door made of hard iron",
                                "1: go to door?","2: stay were you are.", "you make your way to the door and try to open it","you stay and stand around boring ")
        
        story_Two_Questions_Base("As you try to open it you find that your arms are too weak to lift the heavy door.(you need lvl 1 strength!)","you start to think is there anything you can use to lift the door?",
                                "1:search the room?","2: keep trying to lift the door thinking your going to get lucky","as you dig around the dusty room you see somthing shiny its a coin!",
                                "you keep trying to open the door but to your luck you are just so weak it does not move!")
        
        story_Two_Questions_Base("you pick up the coin its super shiny!","the coin looks to have magical properties","1: its a level up coin use it?","2: don't use it",
                                "you use the coin you can now level up one abilty!","you dont use the coin and just stand around come on man lets do somting your stuck in this room!")
        
        story_Two_Questions_Base("you use the coin you know have 1 upgrade point!","what will you use the upgrade point on?","1:strength you would be able ot open the door!",
                                "2: dextertiy then you could do nothing and have level one dexterty!","you level up strength and open the door you are now free!"," are you dumn why would even upgrade that:\ ")
        
        print("this is the end of demo mr teacher i was not able to get the level up system to work and i could not ask you sense i have been sick all this week and missed school im sorry")

   """ """
    storyline_preset_V2(("you wake up and find your self in a dimly lit room","as you stand up and look around you see a big metal door made of hard iron",
    "1: go to door?","2: stay were you are.", "you make your way to the door and try to open it","you stay and stand around boring "))"""
    "chapter_One()"
    wakeup_room_actions = ["search room "," skills ","chill "]
    wakeup_room_storyline=["you wake up and find your self in a dimly lit room","as you stand up and look around you see a big metal door made of hard iron"]
    wakeup_room = Room("wakeup_room", wakeup_room_actions,wakeup_room_storyline)
    wakeup_room.display_user_Input
    wakeup_room.connectedRooms = []
    pass

chapter_One()
