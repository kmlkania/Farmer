from random import choices


class Dice:
    def __init__(self, fields):
        self._fields = fields

    def roll_dice(self):
        population, weights = zip(*self._fields.items())
        return choices(population=population, weights=weights)[0]


class DiceHandler:
    def __init__(self):
        self._green_dice = Dice({'rabbit': 6, 'sheep': 3, 'pig': 1, 'cow': 1, 'wolf': 1})
        self._red_dice = Dice({'rabbit': 6, 'sheep': 3, 'pig': 1, 'horse': 1, 'fox': 1})

    @property
    def get_green_dice(self):
        return self._green_dice

    @property
    def get_red_dice(self):
        return self._red_dice
