import character

def character_Creation():
    print("start Chapter One?")
    print("'press enter twice to continue'")
    char_entry = input()
    if char_entry == input():
        main_Char = str(input("Name your charcter "))
        main_Class = str(input("Whats your class? it can be anything  "))
        main_character = character.character(main_Char,main_Class)

        print("your stats are " + main_character.get_stats())
        return main_character.get_stats()
    else:
        print("error man run again please!")


def story_part(cent,pint,path1,path2):

    """ 
        cent: a centance for first part of the story 
        pint: prints out the next part of story
        path1: what the user may pick currently
        path2: what the user's second option is 
    """

    
    char_Input = input("press enter twice ")
    print(cent)
    if char_Input == input():
        print(pint)
        char_Input = input("press enter twice ")
    else:
         print("error1")
    if char_Input == input():
            print(path1)
    else:
         print("error3")

def story_Two_Questions_Base(centance,centance2,path1,path2,consequence1,consequence2):


    """
    centance1,2: first centance in story line 
    path1,2: diffrent paths user can take
    consequence1/2 is what happens right after user choose path 1 or 2
    """
    
    story_part(centance,centance2,path1,path2,)
    question2 = int(input("1 or 2? "))
    while question2 == 2:
        question2 = print(consequence2)
        question2 = int(input("1 or 2? "))
    else:
        if question2 == 1:
            print(consequence1)
        elif question2 == 2:
            print(consequence2)
        else:
            print("Invalid input.")


"""
Version 2 of my program 
"""

"""
uses a list to write the story then prints it out
first finds length of the list 
then sets the num_Up to 0 to grab the first centance in the list 
next puts the length of the list into the range loop and runs it that many times 
every time it runs it adds a +1 to num_Up until it gets to the last item of the list!
"""

#version two uses a list instead and gets it to answer all you need to do 
#is put in centance frames and your good 

def storyline_preset_V2(story_cent):
    length_Of_List = len(story_cent)
    num_Up = 0
    for i in range(length_Of_List):
        print(story_cent[num_Up])
        input("press enter to continue - >")
        num_Up = num_Up + 1



def storyline_Questions_V2(story_Questions):
    length_Of_Story_Qustions = len(story_Questions)
    user_answer = input("1 or 2 ")
    user_answer
    for i in range(length_Of_Story_Qustions):
        if user_answer == 1:
            print()
        elif user_answer == 2:
            print()
        while user_answer != 1 or 2:
            if user_answer == 1:
                print()
            elif user_answer == 2:
                print()

                
"""
class rooms is a class that you set meaning full stuff in
your rooms for the game there are amount of exits all the options
in the room that you can do npc's to talk to and items you can use
"""

class Room:
    def __init__(self, name, actions, storyline):
        self.name = name
        self.actions = actions
        # self.response = response 
        self.storyline = storyline
        self.connectedRooms = None

    def display_user_Input(self):
        user_Input = input("1:storline inputs,2:exits ")
        print(user_Input)
        numberized = int(user_Input)
        if numberized == 1:
            self.display_actions()
        elif numberized == 2:
           self.display_exits()

    def display_storyline(self):
        print(self.storyline + "\n")

    def display_exits(self):
        print("Exits available in ", self.name + ":")
        number = 1
        for room in self.connectedRooms:
            print("Exit " + str(number) + " -", room.name)
            number += 1
        print("")

    def display_actions(self):
        print("Actions available in", self.name + ":")
        number = 1
        for action in self.actions:
            print(str(number) + " -", action)
            number += 1
        print("")

    def storyline_preset_V2(self,story_cent):
        length_Of_List = len(story_cent)
        num_Up = 0
        for i in range(length_Of_List):
            print(story_cent[num_Up])
            input("press enter to continue - >")
            num_Up = num_Up + 1

# Example usage:
kitchen_actions = ["Open fridge", "Cook meal", "Wash dishes"]
kitchen_storyline = "You find yourself in a small kitchen with a pleasant aroma."

kitchen = Room("Kitchen", kitchen_actions, kitchen_storyline)

livingRoom_actions = ["Go to the Kitchen", "Sit on a sofa"]
livingRoom_storyline = "You find yourself in a small living room, you realize it's a dead end. But theres a sofa."
livingRoom = Room("Living Room", livingRoom_actions, livingRoom_storyline)
kitchen.connectedRooms = [livingRoom]
livingRoom.connectedRooms = [kitchen]

# Display room information
"""kitchen.display_storyline()
kitchen.display_actions()
kitchen.display_exits()"""
kitchen.display_user_Input()

    