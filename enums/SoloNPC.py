from enum import Enum


class SoloNPC(Enum):
    """
    id, level, hp, phys_dmg_red, ele_dmg,red, damage
    """
    snake = 0, 1, 50000, 70, 100, (0, 21)

    @classmethod
    def get_random_npc_two_levels_range(cls, level):
        return_list = []
        for npc in list(cls):
            if level - 2 <= npc.value[1] <= level + 2:
                return_list.append(npc)
        return return_list
