from enum import Enum


class Attributes(Enum):
    """
    Name
    0) ID
    1) True weapon only     False armour only     None both
    2) Base value
    """
    critical_strike_chance = 0, True, 2
    critical_strike_multiplier = 1, True, 3
    global_damage_multiplier = 2, False, 1
    life_steal = 3, True, 1
    energy_regen = 4, None, 1
    max_energy = 5, None, 1
    armor = 7, False, 1
    evasion_rating = 8, False, 1
    poison = 9, True, 1
    poison_resist = 10, False, 1
    elemental_conversion = 11, True, 1
    elemental_resistance = 12, False, 1
    elemental_bonus = 13, True, 1
    armor_penetration = 14, True, 1
    life = 15, False, 1

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.name

    @classmethod
    def get_attribute(cls, id):
        for attribute in list(cls):
            if int(attribute) == id - 65:
                return attribute
        return None
