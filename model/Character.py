from enums.Attributes import Attributes
from enums.Stats import Stats


class Character:
    EQUIPMENT_SLOTS = 5
    ITEM_STORAGE = 20

    def __init__(self, character_name):
        self.available_points = 10
        self.base_stats = dict()
        self.character_stats = dict()
        self.character_name = character_name
        self.worn_equipment = []
        self.character_inventory = []
        self.character_level = 1
        self._init_worn_equip_and_stats()

    def allocate_points(self, amount, stat):
        self.base_stats[stat] += amount
        if self.available_points >= amount:
            self.available_points -= amount
            self.base_stats[stat] += amount
            return True
        return self.available_points

    def _init_worn_equip_and_stats(self):
        for slot in range(self.EQUIPMENT_SLOTS):
            self.worn_equipment += [None]
        for full_stat in list(Stats) + list(Attributes):
            self.character_stats[full_stat] = 0
        for stat in list(Stats):
            self.base_stats[stat] = 5
            self.character_stats[stat] = 5
        return

    def store_item(self, equipment):
        if len(self.character_inventory) >= self.ITEM_STORAGE:
            return False
        else:
            self.character_inventory += [equipment]
        return True

    def drop_item(self, equipment):
        for item in self.character_inventory:
            if item == equipment:
                self.character_inventory.remove(equipment)
                return True
        return False

    def equip_item(self, equipment):
        slots = equipment.get_equipment_type().value[1]
        if len(slots) != 1 and self.worn_equipment[1] is not None and self.worn_equipment[0] is not None and len(
                self.character_inventory) > self.ITEM_STORAGE - 2:
            return False
        self.drop_item(equipment)
        for slot in list(slots):
            if self.worn_equipment[slot] is not None:
                self.store_item(self.worn_equipment[slot])
                self.worn_equipment[slot] = None
        self.worn_equipment[int(slots([slots][0]))] = equipment
        return True

    def __str__(self):
        return "%s level: %d" % (self.character_name, self.character_level)

    def unequip_item(self, equipment):
        if len(self.character_inventory) < self.ITEM_STORAGE:
            self.character_inventory.append(equipment)
            self.worn_equipment[equipment.get_equipment_type().value[1]] = None
            return True
        return False

    def calculate_full_stats(self):
        for full_stat in list(Stats) + list(Attributes):
            self.character_stats[full_stat] = 0

        for stat in self.base_stats:
            self.character_stats[stat] += self.base_stats[stat]
        for item in self.worn_equipment:
            if item is not None:
                for stat in item.get_stats():
                    self.character_stats[stat] += item.get_stats[stat]
        return True
