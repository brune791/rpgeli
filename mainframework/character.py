"""charcter.py 
The base class for the player and any npc in the game. 
will have atributes """

class character:
    """ Any playing and non-playing charcters share these 
    traits
    Attriobutes:
        name: a string 
        class_name:string name if charcter class 
        strength: int physical power carrying capacity defnense 
        dexterity:
        idea: only allow people to level up strength but give them 
    the idea that they can level up all 6 others but someone 
    tells them not too
    
    """
    def __init__(self,name: str, class_name ="") -> None:
        "reprents single charcters with specific names "
        self.name = name
        self.class_name = class_name

        #intializing all remaing stats to 0 (we will creat functions to set them)
        self.strength = 0 
        self.dexterity = 0

    def get_stats(self) -> str:
        """return a formatted string of stats """
        stats = f"Name: {self.name}\nClass: {self.class_name}\n"
        stats += f"strength: {self.strength}\nDexterty: {self.dexterity}"
        return stats





#global scope test 
if __name__ == "__main__":
    player = character("chris","strongman")
    print(player.get_stats())