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




"""story_part("you wake up in a room","you stand up and look around the room, it is dimly lit the only way out is a heavy looking door","1: go try to open door? ", "2:stay where you are? ")\

lool = int(input("1 or 2? "))

user_Answer(lool,"you try to lift the door but its too heavy","you stand around and do nothing boring!")
"""
lool = 2
story_part("you wake up in a room","you stand up and look around the room, it is dimly lit the only way out is a heavy looking door","1: go try to open door? ", "2:stay where you are? ")

while lool == 2:
    lool = int(input("1 or 2? "))
else:
    if lool == 1:
        user_Answer(lool,"you try to lift the door but its too heavy","you stand around and do nothing boring!")
    elif lool == 2:
        user_Answer(lool,"you stand around and do nothing boring!","you try to lift the door but its too heavy")
    else:
        print("Invalid input.")