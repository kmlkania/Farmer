from Herd import HerdHandler
from Dice import DiceHandler
from Player import PlayerHandler


class Game:
    def __init__(self, players_names):
        self.herd = HerdHandler(players_names)
        self.dices = DiceHandler()
        # self.players_names = players_names
        self.players = PlayerHandler({name: self.herd.players_herd[name] for name in players_names})
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
        self.players.players[name].add_animals(results)
        if self.end_turn_callback:
            self.end_turn_callback(name)


