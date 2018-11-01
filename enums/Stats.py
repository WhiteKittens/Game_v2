from enum import Enum


class Stats(Enum):
    """
    Name
    0) ID
    1) No Clue yet
    2) Base value
    """
    Stamina = 0, 0, 5
    Strength = 1, 0, 5
    Intelligence = 2, 0, 5

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.name

    @classmethod
    def get_stat(cls, id):
        for stat in list(cls):
            if int(stat) == id - 65:
                return stat
        return None
