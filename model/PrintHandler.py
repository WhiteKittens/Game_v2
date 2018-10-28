from model.Equipment import Equipment


class PrintHandler:
    PATH = "Dialogue/"
    SPACES = 56

    def __init__(self):
        self.header_footer = "`||" + "=" * 57 + "|| `\n"

    def print_file(self, file_name, ctx):
        file = open((self.PATH + file_name).replace("/", "\\"))

        return_help = self.header_footer
        for line in file:
            line = line.replace("#player", ctx.message.author.display_name).replace("\n", "")
            line += " " * (self.SPACES - len(line)) + "||`"
            line = "`|| " + line
            line += "\n"
            return_help += line
        return return_help + self.header_footer

    def print_equipment(self, equipment, ctx):
        e = Equipment(25)
        return_help = self.header_footer
        for line in str(e).split("\n"):
            line = line.replace("#player", ctx.message.author.display_name).replace("\n", "").replace("\t", " " * 3)
            line += " " * (self.SPACES - len(line)) + "||`"
            line = "`|| " + line
            line += "\n"
            return_help += line
        if return_help.count("\n") < 30:
            return_help += self.header_footer
            return_help += ("`|| " + (" " * self.SPACES) + "||`\n") * (30 - return_help.count("\n") - 1)
        return return_help + self.header_footer
