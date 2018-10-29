from discord.ext.commands import bot

from enums.GameControls import GameControls
from model.GFU import GFU
from view.PrintHandler import PrintHandler


class GameHandlerV2:
    printHandler = PrintHandler()
    client = bot

    def __init__(self, init_bot):
        self.init_bot = init_bot
        self.players = []

    @client.command(pass_context=True)
    async def game(self, ctx):
        await ctx.bot.delete_message(ctx.message)
        image = await ctx.bot.say("Hello welcome to the game!")
        msg = await ctx.bot.say("loading game settings!")
        await self.init_reactions(ctx, image)
        for player in self.players:
            if str(player) == ctx.message.author.id:
                return await player.set_ctx(ctx, image, msg, self.printHandler)
        self.load_player_data(ctx)  # has to check if player has yet to be loaded
        player = GFU(ctx)
        self.players += [player]
        await player.set_ctx(ctx, image, msg, self.printHandler)

    def load_player_data(self, ctx):
        pass

    @staticmethod
    async def init_reactions(ctx, image):
        for smiley in list(GameControls):
            await ctx.bot.add_reaction(image, smiley.value[0])


def setup(init_bot):
    init_bot.add_cog(GameHandlerV2(bot))
