from enum import Enum
from math import log2
from random import choice


class EquipmentType(Enum):
    """
    name
    0) ID
    1) Slots
    2) base_dmg_for_formula
    """
    Helm = 0, 2
    Body = 1, 3
    Legs = 2, 4
    Shield = 3, 1
    Two_handed_sword = 4, (0, 1)
    One_handed_sword = 5, 0
    Daggers = 6, (0, 1)
    Staff = 7, (0, 1)
    Fist_weapons = 8, (0, 1)
    Two_handed_axe = 9, (0, 1)
    One_handed_axe = 10, 0

    def __int__(self):
        return self.value[0]

    def base_damage(self, item_level):
        return log2(len(self.value[1]) ** 2 * (item_level + 7))

    def is_weapon(self):
        return (not isinstance(self.value[1], int)) or (self.value[1] == 0)

    @classmethod
    def random_equipment_type(cls):
        return choice(list(cls))

    @classmethod
    def get_equipment_type(cls, id):
        for equipment in list(cls):
            if int(equipment) == id - 65:
                return equipment
        return None
