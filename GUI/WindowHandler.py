from GUI.PlayerNamesWindow import PlayerNamesWindow
from GUI.GameWindow import GameWindow


class WindowHandler:
    def __init__(self):
        self.current_window = None
        self.players = []

    def __call__(self, *args, **kwargs):
        self.current_window = PlayerNamesWindow()
        self.current_window.setup_main_window()
        self.current_window.set_exit_callback(self.set_players)
        self.current_window.show_window()

    def set_players(self, players):
        self.players = players
        self.start_game()

    def start_game(self):
        self.current_window = GameWindow(self.players)
        self.current_window.setup_window()
        self.current_window.show_window()
