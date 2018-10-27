from enum import Enum
from enums.WeaponType import WeaponType
from enums.Stats import Stats


class GameClasses(Enum):
    """
    Weapons, Stat chart
    """
    warrior = 0, (WeaponType.two_handed_sword, WeaponType.one_handed_sword, WeaponType.axe), \
              ((Stats.Strength, 3), (Stats.Stamina, 3), (Stats.Agility, 1), (Stats.Intelligence, 1))
