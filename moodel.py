class Fill:
    string = ""

    def __init__(self):
        self.string += "**||============================================||**\n"
        self.string += ("**||" + " " * 124 + "||**\n") * 14
        self.string += "**||============================================||**\n"

    def get_str(self):
        return self.string
