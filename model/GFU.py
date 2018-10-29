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

    def character_selection(self):
        pass
