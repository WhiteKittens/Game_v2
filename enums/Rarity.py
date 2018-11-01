from enum import Enum
from random import choice, randint, sample

from enums.Attributes import Attributes
from enums.EquipmentTier import EquipmentTier
from enums.Stats import Stats


class Rarity(Enum):
    """
    Name
    0) ID
    1) Drop_R.
    2) I.lvl.R.
    3) #Stats
    4) #Attributes
    """
    Game_Breaker = 0, 1, 150, 3, 8
    Lost_Relic = 1, 2, 85, 3, 4
    Legendary = 2, 15, 65, 2, 4
    Rare = 3, 100, 45, 2, 3
    Uncommon = 4, 350, 20, 1, 3
    Common = 5, 1000, 1, 1, 2

    @classmethod
    def random_rarity(cls, item_level, rarity_floor=1):
        full_list = []
        for rarity in cls:
            if rarity_floor - 30 <= rarity.value[2] <= item_level:
                full_list += [rarity] * rarity.value[1]
        return choice(full_list)

    def random_stats(self):
        return sample(list(Stats), self.value[3])

    def random_attributes(self, equipment_type):
        full_list = []
        for attribute in list(Attributes):
            if attribute.value[1] == equipment_type.is_weapon() or attribute.value[1] is None:
                full_list += [attribute]
        return sample(full_list, self.value[4])

    def full_stat_dict(self, equipment, floor_rarity=1):
        """
        :rtype: dict
        """
        full_list = dict()
        for stat in self.random_stats() + self.random_attributes(equipment.get_equipment_type()):
            tier = EquipmentTier.random_tier(equipment.get_equipment_level(), floor_rarity)
            slot_bonus = (len(equipment.get_equipment_type().value[1]) +1) / 2
            value = randint(tier.value[2][0], tier.value[2][1]) * stat.value[2] * slot_bonus
            full_list[stat.name] = (tier, value)
        return full_list
