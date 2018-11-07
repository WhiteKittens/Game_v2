from math import log2

from enums.Attributes import Attributes
from enums.Stats import Stats
from model.Equipment import Equipment


class Character:
    EQUIPMENT_SLOTS = 5
    ITEM_STORAGE = 20

    def __init__(self, character_name):
        self.exp = 0
        self.max_life = 0
        self.available_points = 10
        self.base_stats = dict()
        self.character_stats = dict()
        self.character_name = character_name
        self.worn_equipment = []
        self.character_inventory = []
        self.character_level = 100
        self._init_worn_equip_and_stats()
        self.calculate_full_stats()

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
        if isinstance(slots, tuple) and self.worn_equipment[1] is not None and self.worn_equipment[0] is not None and len(
                self.character_inventory) > self.ITEM_STORAGE - 2:
            return False
        self.drop_item(equipment)
        if isinstance(slots, tuple):
            for slot in list(slots):
                if self.worn_equipment[slot] is not None:
                    self.store_item(self.worn_equipment[slot])
                    self.worn_equipment[slot] = None
                self.worn_equipment[int(slots[0])] = equipment
        else:
            if self.worn_equipment[slots] is not None:
                self.store_item(self.worn_equipment[slots])
            self.worn_equipment[int(slots)] = equipment

        self.calculate_full_stats()
        return True

    def __str__(self):
        return "%s level: %d" % (self.character_name, self.character_level)

    def unequip_item(self, equipment):
        if len(self.character_inventory) < self.ITEM_STORAGE:
            self.character_inventory.append(equipment)
            self.worn_equipment[equipment.get_equipment_type().value[1]] = None
            self.calculate_full_stats()
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
                    self.character_stats[stat] += item.get_stats()[stat][1]

        self.calculate_life()
        return True

    def calculate_life(self):
        life = 500 + self.character_level * 5 + (
                (self.character_stats[Stats.Stamina]) * log2(1 + self.character_level)) + log2(
            self.character_stats[Stats.Strength]) * self.character_level
        life += self.character_stats[Attributes.life]
        self.max_life = int(life)

    def get_stats(self):
        return_list = dict()
        for stat in self.character_stats:
            if self.character_stats[stat] != 0:
                return_list[stat] = self.character_stats[stat]
        return return_list

    def encrypt(self):
        encrypt = self.encrypt_name() + str(chr(0))
        encrypt += '0x%04X' % self.available_points + str(chr(0))
        encrypt += '0x%02X' % self.character_level + str(chr(0))
        for stat in self.base_stats:
            encrypt += chr(stat.value[0] + 65)
            encrypt += '0x%04X' % self.base_stats[stat] + str(chr(0))
        for item in self.worn_equipment:
            if item is None:
                encrypt += str(chr(1))
            else:
                encrypt += item.encrypt()
            encrypt += chr(0)
        for item in self.character_inventory:
            encrypt += item.encrypt() + chr(0)
        return encrypt

    def decrypt(self, decryption_string):
        decrypt = decryption_string.split(chr(0))
        self.decrypt_name(decrypt[0])
        self.available_points = int(decrypt[1], 16)
        self.character_level = int(decrypt[2], 16)
        decrypt = decrypt[3:]
        for stat in range(len(list(Stats))):
            self.base_stats[Stats.get_stat(ord(decrypt[0][:1]))] = int(decrypt[0][1:], 16)
            decrypt = decrypt[1:]

        for item in range(self.EQUIPMENT_SLOTS):
            if decrypt[0] == chr(1):
                add = None
            else:
                add = Equipment()
                add.full_import(decrypt[0])

            self.worn_equipment[item] = add
            decrypt = decrypt[1:]
        for item in range(len(decrypt) - 1):
            add = Equipment()
            add.full_import(decrypt[0])
            self.worn_equipment[item] = add
            decrypt = decrypt[1:]
        return True

    def encrypt_name(self):
        encrypted_name = ""
        for char in self.character_name:
            encrypted_name += chr(ord(char) + 124)
        return encrypted_name

    def decrypt_name(self, name):
        encrypted_name = ""
        for char in name:
            encrypted_name += chr(ord(char) - 124)
        self.character_name = encrypted_name
        return encrypted_name
