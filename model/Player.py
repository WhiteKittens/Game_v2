from model.Character import Character


class Player:

    def __init__(self, discord_user_id):
        self.player_id = discord_user_id
        self.characters = dict()
        self.current_character = None

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

    def __str__(self):
        return self.player_id
