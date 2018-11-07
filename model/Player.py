import os
from pathlib import Path

from model.Character import Character


class Player:

    def __init__(self, discord_user_id):
        self.player_id = discord_user_id
        self.characters = dict()
        self.current_character = None
        self.load_player()

    def create_character(self, character_name):
        self.characters[character_name] = Character(character_name)

    def get_characters(self):
        return self.characters

    def set_current_character(self, character_name):
        self.current_character = self.characters[character_name]

    def get_current_character(self):
        return self.current_character

    def player_has_character(self):
        return len(self.characters) != 0

    def save_player(self):
        if self.current_character is not None:
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = "players"
            filename = self.player_id
            filepath = os.path.join(here, subdir, filename)
            f = open(filepath, "w+")
            add = ""
            for character in self.characters:
                add += self.characters[character].encrypt()
            f.write(add)
            print("saved file player to " + filename)
        return

    def load_player(self):
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "players"
        filename = self.player_id
        filepath = os.path.join(here, subdir, filename)
        if not os.path.exists(filepath):
            return
        f = open(filepath)
        for line in f:
            c = Character('fill')
            self.characters[c.decrypt_name(line.split(chr(0))[0])] = c
            c.decrypt(line)

    def __str__(self):
        return self.player_id


# p = Player("058859595")
# p.create_character("jos")
# p.set_current_character("jos")
# p.save_player()
