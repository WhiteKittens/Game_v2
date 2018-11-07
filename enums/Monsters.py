from enum import Enum
from random import choice


class Monsters(Enum):
    """
    id level life damage defence rarity,     drop item / gold,is boss,  picture
    """
    kaaul = 0, 85, 40000, (2000, 2000), (70, 40), 1, (
        100,
        (100, 70000)), True, "https://cdn.discordapp.com/attachments/340501145661341697/508051370704764958/latest.png"

    @classmethod
    def get_monster(cls, zone_level):
        return_list = []
        for monster in list(cls):
            if zone_level - 5 < monster.value[1] < zone_level + 5:
                return_list += [monster] * monster.value[5]
        return choice(return_list)
