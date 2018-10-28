from discord.ext.commands import bot
from model import Fill
from Model.Equipment import Equipment

class GameCommands:
    def __init__(self, sample_bot):
        self.sample_bot = sample_bot

    @bot.command(pass_context=True)
    async def checkreacts(self, ctx):
        await ctx.bot.say("React to me!")
        msg1 = await ctx.bot.say("React to me!")
        await ctx.bot.add_reaction(msg1, '😃')
        while True:
            reaction = await ctx.bot.wait_for_reaction(user=ctx.message.author)
            print(reaction.reaction.emoji)
        # await ctx.bot.say("You responded with {}".format(reaction.reaction.emoji))

    @bot.command(pass_context=True)
    async def start(self, ctx):
        pls = Fill()
        msg = await ctx.bot.say(pls.get_str())
        for emoji in ["⬆", "⬇", "⬅", "➡", "⚔", "🛡", "🏳", "💗", "🗺"]:
            await ctx.bot.add_reaction(msg, emoji)

        while True:
            reaction = await ctx.bot.wait_for_reaction(user=ctx.message.author)
            if reaction.reaction.emoji == "⚔":
                e = Equipment(65, 25)
                await ctx.bot.say(e)

def setup(sample_bot):
    sample_bot.add_cog(GameCommands(bot))


"""
:crossed_swords: = ⚔
:up: = ⬆
:down: ⬇
:left: ⬅
:right: ➡
:shield: 🛡
:flag: 🏳
:world map: 🗺
:hearth: 💗
"""
