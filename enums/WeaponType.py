from enum import Enum
from enums.Stats import Stats
from enums.Attributes import Attributes

MELEE = [Stats.Strength, Stats.Stamina, Stats.Agility]
MAGIC = [Stats.Stamina, Stats.Strength, Stats.Intelligence]

MELEE_ATTR = [Attributes.poison, Attributes.critical_strike_chance,
              Attributes.critical_strike_multiplier, Attributes.life_steal, Attributes.elemental_conversion,
              Attributes.elemental_bonus, Attributes.armor_penetration]
MAGIC_ATTR = [Attributes.poison, Attributes.critical_strike_chance,
              Attributes.critical_strike_multiplier, Attributes.life_steal, Attributes.elemental_conversion,
              Attributes.elemental_bonus]


class WeaponType(Enum):
    """
    value: index , possible stats, possible attributes, equipment slot ,name, is_two_handed
    """
    two_handed_sword = 0, MELEE, MELEE_ATTR, 0, "sword", 1.5
    one_handed_sword = 1, MELEE, MELEE_ATTR, 0, "sword", 1
    dagger = 2, MELEE, MELEE_ATTR, 0, "dagger", 1
    staff = 3, MAGIC, MAGIC_ATTR, 0, "staff", 1.5
    fist_weapon = 4, MELEE, MELEE_ATTR, 0, "fist", 1
    axe = 5, MELEE, MELEE_ATTR, 0, "axe", 1.5

    @classmethod
    def get_two_handed_weapons(cls):
        return_list = []
        for weapon in list(cls):
            if weapon.value[5] != 1:
                return_list.append(weapon)
        return return_list
