from enums.Rarity import Rarity
from enums.WeaponType import WeaponType
from enums.EquipmentTier import EquipmentTier

import random


class Weapon:

    def __init__(self, full_import, item_level=100, floor_rarity=0):
        self.floor_rarity = floor_rarity
        self.item_level = item_level
        self.rarity = Rarity.Game_breaker
        self.equipment_name = ""
        self.equipment_type = Rarity.Game_breaker
        self.equipment_stats = dict()
        self.equipment_attributes = dict()

        if full_import:
            return
        self.initialise_equipment()

    def initialise_equipment(self):
        self.initialise_rarity()
        self.initialise_type()
        self.initialise_name()
        self.initialise_stats_and_attributes()

    def initialise_rarity(self):
        """
        initialises rarity by making a list of all rarities
        containing them once for each percentage of chance at getting them
        :return: None
        """
        rarity = []
        for rar in list(Rarity):
            if self.floor_rarity <= rar.value[4] <= self.item_level:
                rarity += [rar] * rar.value[1]
        self.rarity = random.choice(rarity)

    def initialise_type(self):
        self.equipment_type = random.choice(list(WeaponType))

    def initialise_name(self):
        self.equipment_name = self.equipment_type.value[4]

    def initialise_stats_and_attributes(self):
        stats = random.sample(self.equipment_type.value[1], self.rarity.value[2])
        attributes = random.sample(self.equipment_type.value[2], self.rarity.value[3])
        tier_list = []
        for tier in list(EquipmentTier):
            if self.floor_rarity <= tier.value[4] <= self.item_level:
                tier_list += ([tier] * tier.value[1])

        for stat in stats:
            self.equipment_stats[stat] = self.get_tuple_value_weapon_stats(tier_list, stat)

        for attribute in attributes:
            self.equipment_attributes[attribute] = self.get_tuple_value_weapon_stats(tier_list, attribute)

    def get_tuple_value_weapon_stats(self, tier_list, stat):
        tier = random.choice(tier_list)
        value = round(random.randint(tier.value[2][0], tier.value[2][1]) * stat.value[1] * self.equipment_type.value[5])
        return tier, value

    @staticmethod
    def print_stats(stats):
        for attr in stats:
            print("\t%10s\t%-30s:\t%d" % (stats[attr][0].value[3], attr.name.lower()
                                          , stats[attr][1]))

    def print_weapon(self):
        print(self.equipment_name)
        print(self.rarity.name)
        self.print_stats(self.equipment_stats)
        self.print_stats(self.equipment_attributes)

    def get_equipment_type(self):
        return self.equipment_type

    def get_stats_and_attr(self):
        return dict(self.equipment_attributes.items() | self.equipment_stats.items())
