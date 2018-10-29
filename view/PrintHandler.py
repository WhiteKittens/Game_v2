from discord import Embed

from enums.GameControls import GameControls


class PrintHandler:
    TOP_SIZE = 10
    BOT_SIZE = 20
    PATH = "Dialogue/"
    IMAGE_PATH = "pictures/"
    SPACES = 56

    def __init__(self):
        self.header_footer = "`||" + "=" * 57 + "|| `\n"

    async def handle_screen(self, ctx, msg, image, screen, items=None, selected=0):
        await self.set_image(image, screen.value[10], ctx)
        if screen.value[9] is not None:
            header = await self.get_header(screen.value[9], ctx)
        else:
            header = "Still not done i guess"
        if screen.value[11] is None:
            footer = self.add_length("", self.BOT_SIZE)
        elif screen.value[11] == "selector_list":
            footer = "Still i fcked up"
        else:
            footer = "xd"
        await ctx.bot.edit_message(msg, header + footer)

    @staticmethod
    async def cleanup(ctx, image, msg):
        await ctx.bot.delete_message(image)
        await ctx.bot.delete_message(msg)

    @staticmethod
    async def wait_on_control(ctx, image):
        done = False
        while not done:
            reaction = await ctx.bot.wait_for_reaction(GameControls.all_emojis(), message=image)
            await ctx.bot.remove_reaction(image, reaction.reaction.emoji, reaction.user)
            key = GameControls.get_emojis(reaction.reaction.emoji)
            if key is not None:
                return key
        return

    @staticmethod
    async def set_image(image, url, ctx):
        await ctx.bot.edit_message(image, new_content=ctx.message.author.display_name + "'s game session:",
                                   embed=Embed().set_image(url=url))

    async def get_header(self, file_name, ctx):
        final_header = self.header_footer
        file = open((self.PATH + file_name).replace("/", "\\"))
        for line in file:
            line = line.replace("#player", ctx.message.author.display_name).replace("\n", "").replace("\t", " " * 3)
            line += " " * (self.SPACES - len(line)) + "||`"
            line = "`|| " + line
            line += "\n"
            final_header += line
        return self.add_length(final_header, self.TOP_SIZE)

    def add_length(self, msg, length):
        if msg.count("\n") < 30:
            msg += ("`|| " + (" " * self.SPACES) + "||`\n") * (length - msg.count("\n") - 1)
            msg += self.header_footer
        return msg
