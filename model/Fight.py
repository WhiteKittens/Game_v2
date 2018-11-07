from math import log2
from random import randint

from enums.Attributes import Attributes
from enums.EquipmentType import EquipmentType
from enums.Monsters import Monsters
from enums.Stats import Stats
from model.Equipment import Equipment
from model.Player import Player


class Fight:

    def __init__(self, player, print_handler):
        self.player = player
        self.print_handler = print_handler

    def calc_player_dmg(self, character, monster):
        weapon = character.worn_equipment[0]
        if character.worn_equipment[0] is None:
            dmg = 2
        else:
            dmg = weapon.get_equipment_type().base_damage(weapon.get_equipment_level())

        return dmg

    def fight_monster(self, zone_level):
        monster = Monsters.get_monster(zone_level)
        character = self.player.get_current_character()

        character_life = character.max_life
        monster_life = monster.value[2]
        finished = False
        while not finished:
            print(self.calc_player_dmg(character, monster))
            finished = True


p = Player("058859595")
p.create_character("jos")
p.set_current_character("jos")
e = Equipment(100)
e.equipment_type = EquipmentType.Two_handed_axe
p.get_current_character().equip_item(e)

f = Fight(p, None)
f.fight_monster(85)
