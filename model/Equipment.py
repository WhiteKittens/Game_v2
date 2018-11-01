from enums.EquipmentType import *
from enums.Rarity import *


class Equipment:
    rarity: Rarity
    equipment_stats: dict

    def __init__(self, item_level=1, rarity_floor=1):
        self.item_level = item_level
        self.equipment_type = EquipmentType.random_equipment_type()
        self.initialise_random(rarity_floor)

    def __str__(self):
        return_string = ""
        return_string += "%s:\n" % self.equipment_type.name.replace("_", " ")
        return_string += "  Rarity: %s\n\titemlevel: %s" % (
        self.rarity.name.lower().replace("_", " ").capitalize(), self.item_level)
        for stat in self.equipment_stats:
            return_string += "\n\t\t%-8s%-28s:  %6.0f" % (
                self.equipment_stats[stat][0].value[3], str(stat).lower().replace("_", " "),
                self.equipment_stats[stat][1])
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

    def full_import(self, str_equipment):
        self.rarity = Rarity.get_rarity(int(str_equipment[0:1]))
        self.equipment_type = EquipmentType.get_equipment_type(ord(str_equipment[1:2]))
        self.item_level = int(str_equipment[2:6], 16)
        str_equipment = str_equipment[6:]
        self.equipment_stats.clear()
        for stat in range(self.rarity.value[3]):
            val_tuple = (EquipmentTier.get_tier(int(str_equipment[1:2])),
                         int(str_equipment[2:6], 16))
            self.equipment_stats[Stats.get_stat(ord(str_equipment[0:1]))] = val_tuple
            str_equipment = str_equipment[6:]

        for stat in range(self.rarity.value[4]):
            val_tuple = (EquipmentTier.get_tier(int(str_equipment[1:2])),
                         int(str_equipment[2:6], 16))
            self.equipment_stats[Attributes.get_attribute(ord(str_equipment[0:1]))] = val_tuple
            print(val_tuple)
            str_equipment = str_equipment[6:]


a = "3J0x01A00xf8C30xf7A00xf8B40x02C00xf8"
e = Equipment()
e.full_import(a)
print(e)
