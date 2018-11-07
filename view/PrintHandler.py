from discord import Embed
from time import sleep
from enums.GameControls import GameControls


class PrintHandler:
    TOP_SIZE = 8
    BOT_SIZE = 12
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
            footer = self.selector_list_footer(items, selected, ctx)
        else:
            footer = "xd"
        await ctx.bot.edit_message(msg, header + footer)
        val = await self.wait_on_control(ctx, image, screen)
        return val

    def selector_list_footer(self, items, selected, ctx):
        footer = ""
        for item in range(len(items)):
            line = list(items)[item].replace("#player", ctx.message.author.display_name).replace("\n", "").replace(
                "\t", " " * 3)
            if item == selected:
                line += " <<--"
            line += " " * (self.SPACES - len(line)) + "||`"
            line = "`|| " + line
            line += "\n"
            footer += line

        return self.add_length(footer, self.BOT_SIZE)

    @staticmethod
    async def cleanup(ctx, image, msg):
        await ctx.bot.delete_message(image)
        await ctx.bot.delete_message(msg)

    @staticmethod
    async def wait_on_control(ctx, image, screen):
        done = False
        while not done:
            reaction = await ctx.bot.wait_for_reaction(GameControls.all_emojis(), message=image)
            await ctx.bot.remove_reaction(image, reaction.reaction.emoji, reaction.user)
            key = GameControls.get_emojis(reaction.reaction.emoji)
            if key is not None:
                return screen.value[key]
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
