from enums.GameClasses import GameClasses
from enums.WeaponType import WeaponType
from model.Equipment import Equipment
from enums.Stats import Stats
from enums.Attributes import Attributes
from model.Weapon import Weapon
import random


class Character:
    AMOUNT_OF_EQUIPMENT_SLOTS = 5
    BASE_STATS = 5

    def __init__(self, character_name, character_class=GameClasses.warrior):
        self.character_class = character_class
        self.character_name = character_name
        self.character_inventory = list()
        self.character_full_stats = dict()
        self.equipped_items = []

        self.character_level = 100
        self.hp = 0
        self.energy = 0
        self.max_hp = 0
        self.max_energy = 0

        self.init_equipment_slots()
        self.init_stats()

    def init_equipment_slots(self):
        for equipment_slot in range(self.AMOUNT_OF_EQUIPMENT_SLOTS):
            self.equipped_items += [None]

    def add_to_inventory(self, item):
        self.character_inventory.append(item)

    def remove_from_inventory(self, item):
        self.character_inventory.remove(item)

    def equip_item(self, item):
        if item.get_equipment_type in WeaponType.get_two_handed_weapons():
            if self.equipped_items[1] is not None:
                self.character_inventory.append(self.equipped_items[1])
                self.equipped_items[1] = None

        if self.equipped_items[item.get_equipment_type().value[3]] is not None:
            self.character_inventory.append(self.equipped_items[item.get_equipment_type().value[3]])
        self.equipped_items[item.get_equipment_type().value[3]] = item
        self.recalculate_stats()

    def de_equip_item(self, item):
        self.equipped_items[item.get_equipment_type().value[3]] = None
        self.recalculate_stats()

    def init_stats(self):
        for stat in list(self.character_class.value[2]):
            self.character_full_stats[
                stat[0]] = self.BASE_STATS + stat[1] * self.character_level
        for attribute in list(Attributes):
            self.character_full_stats[attribute] = 0

    def recalculate_stats(self):
        self.init_stats()
        for item in self.equipped_items:
            if item is not None:
                print(item.get_stats_and_attr())
                for stat in item.get_stats_and_attr():
                    self.character_full_stats[stat] += item.get_stats_and_attr()[stat][1]
        self.calc_max_hp()

    def print_character_stats(self):
        for stat in self.character_full_stats:
            if 0 < self.character_full_stats[stat]:
                print("%-28s  : %4d" % (stat.name.replace("_", " "), self.character_full_stats[stat]))
        return

    def calc_dmg_unrefined(self):
        min_role = 5
        critical_multiplier = 0
        critical_splat = ""
        if 95 - self.character_full_stats[Attributes.critical_strike_chance] <= random.randint(0, 100) and \
                self.character_full_stats[Attributes.critical_strike_chance] != 0:
            min_role = self.character_level + 5
            critical_multiplier = 70 + self.character_full_stats[Attributes.critical_strike_multiplier]
            critical_splat = "Critical"
        phys_dmg = round(((random.randint(min_role, self.character_level + 14) * 15 * self.character_full_stats[
            Stats.Strength] / 20)) * (1 + critical_multiplier / 100) * ((self.character_full_stats[
                                                                             Attributes.global_damage_multiplier] / 100) + 1))
        phys_dmg += self.character_full_stats[Stats.Agility] * self.character_level
        elemental_dmg = phys_dmg * self.character_full_stats[Attributes.elemental_bonus] + phys_dmg \
                        * self.character_full_stats[Attributes.elemental_conversion]
        phys_dmg *= (100 - self.character_full_stats[Attributes.elemental_conversion])
        return critical_splat, phys_dmg, elemental_dmg

    def calc_max_hp(self):

        self.max_hp = (self.character_full_stats[Stats.Strength] * 632) + (self.character_full_stats[
                                                                               Stats.Stamina] * 63) + 976 * \
                      self.character_level + 11111
        print(self.max_hp)
        print(self.calc_dmg_unrefined())


weapon = Weapon(False, 100, 100)
equipment = Equipment(False, 100, 100)
character = Character("my char")
character.add_to_inventory(weapon)
character.add_to_inventory(equipment)
character.equip_item(weapon)
character.equip_item(equipment)
character.print_character_stats()
character.de_equip_item(weapon)
character.print_character_stats()
