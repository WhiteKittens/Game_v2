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

    async def handle_screen(self, ctx, msg, image, screen):
        await self.set_image(image, screen.value[10], ctx)
        if screen.value[9] is not None:
            header = await self.get_header(screen.value[9], ctx)
        else:
            header = "Still not done i guess"

        await ctx.bot.edit_message(msg, header)

    @staticmethod
    async def set_image(image, url, ctx):
        await ctx.bot.edit_message(image, new_content="", embed=Embed().set_image(url=url))

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

    async def get_print_options(self, text, options, game_handler, ctx):
        current_selected = 0
        header = ""
        for line in text:
            header += line
        header += "\n"
        while True:
            option_string = header
            for option in range(len(list(options))):
                option_string += (list(options)[option])
                if current_selected == option:
                    option_string += " <<--"
                option_string += "\n"
            await ctx.bot.edit_message(game_handler.msg_screen, self.print((option_string + "\n").split("\n"), ctx))

            emoji = await game_handler.wait_on_control(
                [GameControls.SWORDS.value[0], GameControls.DOWN.value[0], GameControls.UP.value[0],
                 GameControls.SHIELD.value[0]])

            if emoji == GameControls.UP.value[0]:
                current_selected -= 1
                if current_selected == -1:
                    current_selected = len(list(options)) - 1
            elif emoji == GameControls.DOWN.value[0]:
                current_selected += 1
                if current_selected == len(list(options)):
                    current_selected = 0
            elif emoji == GameControls.SWORDS.value[0]:
                return list(options)[current_selected]
            elif emoji == GameControls.SHIELD.value[0]:
                return None
