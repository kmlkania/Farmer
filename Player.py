from Herd import PlayerHerd


class Player:
    def __init__(self, herd):
        self.herd = herd

    @property
    def has_won(self):
        return False

    def add_animals(self, roll_result):
        if roll_result[0] == roll_result[1]:
            self.herd.add_animal(roll_result[0], 2)
        else:
            self.herd.add_animal(roll_result[0])
            self.herd.add_animal(roll_result[1])


class PlayerHandler:
    def __init__(self, players):
        self.players = {name: Player(herd) for name, herd in players.items()}
        self._is_winner = False

    @property
    def has_winner(self):
        self._is_winner = any(player.has_won for player in self.players.values())
        return self._is_winner
