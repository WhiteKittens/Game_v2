class Character:
    EQUIPMENT_SLOTS = 5
    ITEM_STORAGE = 20

    def __init__(self, character_name):
        self.character_name = character_name
        self.worn_equipment = []
        self.character_inventory = []

        self._init_character_inventory()

    def _init_character_inventory(self):
        for slot in range(self.EQUIPMENT_SLOTS):
            self.worn_equipment += [None]
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
