import discord
from discord.ext.commands import bot

from enums.GameControls import GameControls
from model.Player import Player
from model.PrintHandler import PrintHandler


class GameHandler:
    x = PrintHandler()
    e = discord.Embed()

    def __init__(self, sample_bot):
        self.msg = None
        self.ctx = None
        self.player = None
        self.sample_bot = sample_bot

    @bot.command(pass_context=True)
    async def start(self, ctx):
        self.ctx = ctx
        self.player = Player(ctx.message.author.id)
        await self.login_screen()

    async def login_screen(self):
        await self.init_image()
        if not self.player.player_has_character():
            await self.ctx.bot.say(self.x.print_equipment("WelcomeScreen.txt", self.ctx))
        else:
            await self.ctx.bot.say("LOLOL")

    async def init_image(self):
        self.e.set_image(
            url="https://cdn.discordapp.com/attachments/501831331035086861/506085028392992768/DarkForest.png")
        self.msg = await self.ctx.bot.send_message(self.ctx.message.channel, embed=self.e)
        await self.set_controls()

    async def set_controls(self):
        for smiley in list(GameControls):
            await self.ctx.bot.add_reaction(self.msg, smiley.value[0])

    async def change_background(self):
        self.e.set_image(url="https://cdn.discordapp.com/attachments/505792603430715395/505792679657865240/latest.png")
        await self.ctx.bot.edit_message(self.msg, embed=self.e)

    async def get_ctx(self):
        return self.ctx


def setup(sample_bot):
    sample_bot.add_cog(GameHandler(bot))
