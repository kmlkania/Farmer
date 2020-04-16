from Herd import Herd


class Player:
    def __init__(self):
        self.herd = Herd()

    @property
    def has_won(self):
        return False


class PlayerHandler:
    def __init__(self, names):
        self.players = {name: Player() for name in names}
        self._is_winner = False

    @property
    def has_winner(self):
        self._is_winner = any(player.has_won for player in self.players.values())
        return self._is_winner
