from Herd import HerdHandler
from Dice import DiceHandler


class Game:
    def __init__(self, players_names):
        self.herd = HerdHandler(players_names)
        self.dices = DiceHandler()
        self.end_turn_callback = None
        self.info_callback = None

    def set_end_turn_callback(self, callback):
        self.end_turn_callback = callback

    def set_info_callback(self, callback):
        self.info_callback = callback

    def make_roll(self, name):
        results = [self.dices.green_dice.roll_dice(), self.dices.red_dice.roll_dice()]
        if self.info_callback:
            self.info_callback('{} rolled out: {}'.format(name, ' and '.join(results)))
        self.herd.reproduce_animals(name, results)
        if self.end_turn_callback:
            self.end_turn_callback(name)

    def sell_animals(self, player, animals):
        self.herd.sell_animals(player, animals)

    def buy_animals(self, player, animals):
        self.herd.buy_animals(player, animals)

    def get_common_herd(self):
        return self.herd.get_common_herd()

    def get_player_herd(self, name):
        return self.herd.get_player_herd(name)

