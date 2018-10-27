from enum import Enum


class EquipmentTier(Enum):
    """
    value: index, drop rate in %, multiplier brackets, drop_limiter
    """
    tier_0 = 0, 1, (30, 30), "Tier 0", 100
    tier_1 = 1, 4, (22, 25), "Tier 1", 99
    tier_2 = 2, 16, (17, 19), "Tier 2", 60
    tier_3 = 3, 28, (13, 15), "Tier 3", 35
    tier_4 = 4, 42, (9, 11), "Tier 4", 15
    tier_5 = 5, 90, (5, 7), "Tier 5", 5
    tier_6 = 6, 160, (1, 3), "Tier 6", 1
