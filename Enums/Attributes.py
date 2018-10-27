from enum import Enum


class Attributes(Enum):
    critical_strike_chance = 0, 1
    critical_strike_multiplier = 1, 1
    global_damage_multiplier = 2, 1
    life_steal = 3, 0.2
    energy_regen = 4, 1
    max_energy = 5, 1
    percent_life = 6, 1
    armor = 7, 1
    evasion_rating = 8, 1
    poison = 9, 1
    poison_resist = 10, 1
    elemental_conversion = 11, 1
    elemental_resistance = 12, 1
    elemental_bonus = 13, 1
    armor_penetration = 14, 1
    life = 15, 45
