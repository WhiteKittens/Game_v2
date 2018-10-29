from enums.GameControlSettings import GameControlSettings
from model.Player import Player


class GFU:

    def __init__(self, ctx):
        self.player = Player(ctx.message.author.id)
        self.ctx = None
        self.image = None
        self.msg = None
        self.print_handler = None

    def __str__(self):
        return str(self.player)

    async def set_ctx(self, ctx, image, msg, print_handler):
        self.ctx = ctx
        self.image = image
        self.msg = msg
        self.print_handler = print_handler
        await self.welcome_screen()

    async def welcome_screen(self):
        val = await self.print_handler.handle_screen(self.ctx, self.msg, self.image, GameControlSettings.WELCOME_SCREEN)
        if val == 0:
            await self.character_selection()
        elif val == 1:
            await self.print_handler.cleanup(self.ctx, self.image, self.msg)
            return
        return

    async def character_selection(self):
        selected = 0
        val = 0
        while val in [0, 1, 3, 4]:
            val = await self.print_handler.handle_screen(self.ctx, self.msg, self.image,
                                                         GameControlSettings.CHARACTER_SELECTION,
                                                         self.player.get_characters(), selected)
            if val == 0:
                if self.player.player_has_character():
                    selected -= 1
                    if selected < 0:
                        selected = len(self.player.get_characters()) - 1
            elif val == 1:
                if self.player.player_has_character():
                    selected += 1
                if selected == len(self.player.characters):
                    selected = 0
            elif val == 2:
                self.player.set_current_character(list(self.player.get_characters())[selected])
            elif val == 3:
                self.player.create_character(self.ctx.message.author.display_name)
                selected = len(self.player.get_characters()) - 1
            elif val == 4:
                self.player.set_current_character(list(self.player.get_characters())[selected])
                selected -= 1
        return
