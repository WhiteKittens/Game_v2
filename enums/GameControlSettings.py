from enum import Enum


class GameControlSettings(Enum):
    """
     0     1       2       3         4         5        6       7       8       9       10      11
    UP == DOWN == LEFT == RIGHT == SWORD == SHIELD == FLAG == HEARTH == MAP == FILE == IMAGE == TYPE
    """
    WELCOME_SCREEN = None, None, None, None, 0, 1, None, None, None, 'WELCOME_SCREEN', \
                     'https://cdn.discordapp.com/attachments/355395847392985091/506151408488284173/2.png', None
    CHARACTER_SELECTION = 0, 1, None, None, 2, 3, 4, None, None, 'CHARACTER_SELECTION', \
                          'https://cdn.discordapp.com/attachments/505792603430715395/505793280248905743/latest.png', \
                          "selector_list"
    MAIN_MENU = 0, 1, None, None, 2, 3, None, 4, 5, \
                "MAIN_MENU", 'https://cdn.discordapp.com/attachments/505792603430715395/505793280248905743/latest.png', \
                "selector_list", ["Inventory", "Set spells", "Shop", "coming soon", "..."]
