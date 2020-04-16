from Herd import HerdHandler
from Dice import DiceHandler
from Player import PlayerHandler


class Game:
    def __init__(self, players_names):
        self.herd = HerdHandler(players_names)
        self.dices = DiceHandler()
        self.players_names = players_names
        self.players = PlayerHandler(self.players_names)

    def start(self):
        iteration = 0
        while not self.players.has_winner:
            player_id = iteration % len(self.players_names)
            print('player {} yours herd is'.format(self.players_names[player_id]))
            print(self.players[player_id].show_herd)
            iteration += 1


