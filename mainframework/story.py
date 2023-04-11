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

def enter_func(cent,pint,ans,action1,action2):
    """ cent: a centance for first part of the story 
        pint: prints out the next part of story 
        ans: the answer to the question in cent from the user 
        action1 the first andswer the user can take 
        action2 the second answer the user can take
    """
    print(cent)
    char_Input = input("press enter twice ")
    if char_Input == input():
        print(pint)
        input(ans)
        if ans == 1:
            print(action1)
        else:
            print(action2)
    else:
        ("error man")


def chapter_One():
    
    enter_func("you wake up in a room","you stand up and look around the room is dimly lit the only way out is a heavy looking door",ans1," 1:go to door and try to open it?","2: stay where you are.")
    ans1 = input("one or two")


chapter_One()

