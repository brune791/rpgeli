import character


def character_Creation():
    print("start Chapter One?")
    print("'press enter twice to  continue'")
    char_entry = input()
    if char_entry == input():
        main_Char = str(input("Name your charcter "))
        main_Class = str(input("Whats your class? "))
        main_character = character.character(main_Char,main_Class)

        print("your stats are " + main_character.get_stats())
    else:
        print("error man run again please!")
#character_Creation()

def story_part(cent,pint,path1,path2):
    """ 
        cent: a centance for first part of the story 
        pint: prints out the next part of story
        path1: what the user may pick currently
        path2: what the user's second option is 
    """
    print(cent)
    char_Input = input("press enter twice ")
    if char_Input == input():
        print(pint)
        char_Input = input("press enter twice ")
    else:
         print("error1")
    if char_Input == input():
            print(path1)
            print(path2)
    else:
         print("error3")

def user_Answer(ans,consequence1,consequence2):
    """
        ans: the answer to the question in cent from the user 
        consequence1,2: are what happens right after user chose path 1 or 2 from function story_part
    """
    if ans == 1:
         print(consequence1)
    elif ans == 2:
         print(consequence2)
    else:
         print("error restart game:(")