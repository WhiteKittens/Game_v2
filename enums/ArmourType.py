from enum import Enum
from enums.Stats import Stats
from enums.Attributes import Attributes

STATS = [Stats.Stamina, Stats.Agility, Stats.Intelligence, Stats.Strength]
ATTR = [Attributes.armour, Attributes.energy_regen, Attributes.evasion_rating, Attributes.max_energy,
        Attributes.poison_resist, Attributes.elemental_resistance, Attributes.life]


class ArmourType(Enum):
    """
    value: index , possible stats, possible attributes
    """
    helm = 0, STATS, ATTR, 2, "helm", 1
    body = 1, STATS, ATTR, 3, "body", 1
    legs = 2, STATS, ATTR, 4, "legs", 1
    shield = 3, STATS, ATTR, 1, "shield", 1
