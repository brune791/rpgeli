from mainframework import character
from io import StringIO


if __name__ == "__main__":
    player = character("chris","strongman")
    print(player.get_stats())