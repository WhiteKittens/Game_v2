from enum import Enum


class Rarity(Enum):
    """
    value: index, drop rate in %,  #stats, #attributes, drop_limiter
    """
    Game_breaker = 0,  1, 3, 5, 100
    Common       = 1, 50, 1, 2,  1
    Uncommon     = 2, 25, 1, 3, 30
    Rare         = 3, 20, 2, 3, 45
    Legendary    = 4,  5, 2, 4, 60
