"""utilties
a set of functions to be used to make the program more useful and be used in other 
simlar projects """

# import statements

def get_Menu_Choice(menu: str, legal_choices: tuple) -> str:
    """displayes a menu of options, and asks the user to make a choice. 
    
    
Args:
    menu: a formatted string of choices for the user 
    legal_choices: a tuple of only choices that the user is allowed to make 

    returns:
        user_ choice: a single charcter that must be one of the legal choices  
    """
