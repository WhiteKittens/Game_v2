from enum import Enum


class GameControlSettings(Enum):
    """
     0     1       2       3         4         5        6       7       8       9       10
    UP == DOWN == LEFT == RIGHT == SWORD == SHIELD == FLAG == HEARTH == MAP == FILE == IMAGE
    """
    WELCOME_SCREEN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 'WELCOME_SCREEN', 'https://cdn.discordapp.com/attachments/355395847392985091/506151408488284173/2.png'
    CHARACTER_SELECTION = 0, 1, None, None, 2, 3, 4, None, None, 'CHARACTER_SELECTION', 'DarkForest.png'
