from enums.Attributes import *
from enums.EquipmentTier import *
from enums.EquipmentType import *
from enums.Stats import *
from enums.Rarity import *


class Equipment:
    rarity: Rarity
    equipment_stats: dict

    def __init__(self, item_level, rarity_floor=1):
        self.item_level = item_level
        self.equipment_type = EquipmentType.random_equipment_type()
        self.initialise_random(rarity_floor)

    def __str__(self):
        return_string = ""
        return_string += "%s:\n" % self.equipment_type.name.replace("_", " ")
        return_string += "  Rarity: %s" % self.rarity.name.lower().replace("_", " ").capitalize()
        for stat in self.equipment_stats:
            return_string += "\n\t\t%-8s%-28s:  %6.0f" % (
                self.equipment_stats[stat][0].value[3], stat.lower().replace("_", " "), self.equipment_stats[stat][1])
        return return_string

    def initialise_random(self, rarity_floor):
        self.rarity = Rarity.random_rarity(self.item_level, rarity_floor)
        self.equipment_stats = self.rarity.full_stat_dict(self, rarity_floor)

    def get_equipment_level(self):
        return self.item_level

    def get_equipment_type(self):
        return self.equipment_type

    def get_stats(self):
        return self.equipment_stats

