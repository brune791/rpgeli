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



def storyline_preset_V2(story_cent):
    length_Of_List = len(story_cent)
    num_Up = 0
    for i in range(length_Of_List):
        print(story_cent[num_Up])
        input("press enter to continue - >")
        num_Up = num_Up + 1 

def storyline_Questions_V2(story_Questions):
    length_Of_List = len(story_Questions)
    user_answer = input("1 or 2 ")
    for i in range(length_Of_List):
        if user_answer == 1:
            print()