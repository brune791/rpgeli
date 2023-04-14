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

