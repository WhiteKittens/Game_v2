from enum import Enum
from math import log2


class EquipmentType(Enum):
    """
    name
    0) ID
    1) Slots
    2) base_dmg_for_formula
    """
    helm = 0, 2
    body = 1, 3
    legs = 2, 4
    shield = 3, 1
    two_handed_sword = 4, (0, 1)
    one_handed_sword = 5, 0
    daggers = 6, (0, 1)
    staff = 7, (0, 1)
    fist_weapons = 8, (0, 1)
    two_handed_axe = 9, (0, 1)
    one_handed_axe = 10, 0

    def base_damage(self, item_level):
        return log2(len(self.value[1]) * (item_level + 7))

    def is_weapon(self):
        return (not isinstance(self.value[1], int)) or (self.value[1] == 0)



