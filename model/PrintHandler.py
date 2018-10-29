from enums.GameControls import GameControls


class PrintHandler:
    PATH = "Dialogue/"
    SPACES = 56

    def __init__(self):
        self.header_footer = "`||" + "=" * 57 + "|| `\n"

    def print_file(self, file_name, ctx):
        file = open((self.PATH + file_name).replace("/", "\\"))
        return self.print(file, ctx)

    def print(self, file, ctx):
        return_help = self.header_footer
        for line in file:
            line = line.replace("#player", ctx.message.author.display_name).replace("\n", "").replace("\t", " " * 3)
            line += " " * (self.SPACES - len(line)) + "||`"
            line = "`|| " + line
            line += "\n"
            return_help += line
        if return_help.count("\n") < 30:
            return_help += self.header_footer
            return_help += ("`|| " + (" " * self.SPACES) + "||`\n") * (30 - return_help.count("\n") - 1)
        return return_help + self.header_footer

    def print_equipment(self, equipment, ctx):
        return self.print(str(equipment).split("\n"), ctx)

    async def get_print_options(self, text, options, game_handler, ctx):
        current_selected = 0
        while True:
            option_string = ""
            for option in range(len(list(options))):
                option_string += list(options)[option]
                if current_selected == option:
                    option_string += " <<--"
                option_string += "\n"
            await ctx.bot.edit_message(game_handler.msg_screen, self.print((option_string + "\n").split("\n"), ctx))
            emoji = await game_handler.wait_on_control(
                [GameControls.SWORDS.value[0], GameControls.DOWN.value[0], GameControls.UP.value[0]])
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
