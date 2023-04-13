from story_func import character_Creation
from story_func import story_part
from story_func import user_Answer


def chapter_One():
    while lool == 2:
        story_part("you wake up in a room","you stand up and look around the room, it is dimly lit the only way out is a heavy looking door","1: go try to open door? ", "2:stay where you are? ")
        lool = int(input("1 or 2?"))
    else:
        user_Answer(lool,"you try to lift the door but its too heavy","you stand around and do nothing boring!")





chapter_One()