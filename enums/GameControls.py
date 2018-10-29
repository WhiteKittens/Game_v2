from enum import Enum


class GameControls(Enum):
    """

    """
    UP = "⬆", 0
    DOWN = "⬇", 1
    LEFT = "⬅", 2
    RIGHT = "➡", 3
    SWORDS = "⚔", 4
    SHIELD = "🛡", 5
    FLAG = "🏳", 6
    HEARTH = "💗", 7
    WORLD = "🗺", 8

    @classmethod
    def all_emojis(cls):
        return_list = []
        for emoji in list(cls):
            return_list += [emoji.value[0]]
        return return_list

    @classmethod
    def get_emojis(cls, searched):
        for emoji in list(cls):
            if emoji.value[0] == searched:
                return emoji.value[1]
        return None
