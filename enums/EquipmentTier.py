from enum import Enum
from random import choice


class EquipmentTier(Enum):
    """
    Name
    0) index
    1) drop rate in %
    2) multiplier brackets
    3) full name
    4) I.lvl.R.
    """
    tier_0 = 0, 1, (30, 30), "Tier 0", 100
    tier_1 = 1, 4, (22, 25), "Tier 1", 99
    tier_2 = 2, 16, (17, 19), "Tier 2", 60
    tier_3 = 3, 42, (13, 15), "Tier 3", 35
    tier_4 = 4, 65, (9, 11), "Tier 4", 15
    tier_5 = 5, 75, (5, 7), "Tier 5", 5
    tier_6 = 6, 110, (1, 3), "Tier 6", 1

    def __int__(self):
        return self.value[0]

    @classmethod
    def random_tier(cls, item_level, floor_rarity=1):
        full_list = []
        for tier in list(cls):
            if (floor_rarity - 40) <= tier.value[4] <= item_level:
                full_list += [tier] * tier.value[1]
        return choice(full_list)

    @classmethod
    def get_tier(cls, id):
        for tier in list(cls):
            if int(tier) == id:
                return tier
        return None
