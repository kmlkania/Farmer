from PyQt5 import QtWidgets
from Game import Game


class GameWindow:
    def __init__(self, players):
        self.window = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout()
        self.players_names = players
        self.game = Game(players)
        self.window.setLayout(self.grid_layout)
        self.common_view_items = {}
        self.players_view = {}

    def setup_window(self):
        self.window.setWindowTitle('Farmer Game')
        self.configure_common_widget()
        self.configure_player_widget()
        self.update_view()

    def configure_common_widget(self):
        common_widget = QtWidgets.QWidget()
        inside_grid = QtWidgets.QGridLayout()
        common_widget.setLayout(inside_grid)
        self.grid_layout.addWidget(common_widget, 0, 0, 1, 1)
        lbl = QtWidgets.QLabel()
        lbl.setText('common herd:')
        inside_grid.addWidget(lbl, 0, 0, 1, 1)
        animals = self.game.herd.common.herd
        self.common_view_items = {animal: QtWidgets.QLabel(common_widget) for animal in animals.keys()}
        for i, item in enumerate(self.common_view_items.items()):
            lbl = QtWidgets.QLabel(common_widget)
            lbl.setText(item[0])
            inside_grid.addWidget(lbl, i+ 1, 0, 1, 1)
            inside_grid.addWidget(item[1], i+ 1, 1, 1, 1)

    def configure_player_widget(self):
        for i, name in enumerate(self.players_names):
            player_widget = QtWidgets.QWidget()
            self.grid_layout.addWidget(player_widget, 1, i, 1, 1)
            inside_grid = QtWidgets.QGridLayout()
            player_widget.setLayout(inside_grid)
            lbl = QtWidgets.QLabel()
            lbl.setText(name)
            inside_grid.addWidget(lbl, 0, 0, 1, 1)
            animals = self.game.herd.players_herd[name].herd
            self.players_view.update({name: {animal: QtWidgets.QLabel() for animal in animals.keys()}})
            for i, item in enumerate(self.players_view[name].items()):
                lbl = QtWidgets.QLabel()
                lbl.setText(item[0])
                inside_grid.addWidget(lbl, i+ 1, 0, 1, 1)
                inside_grid.addWidget(item[1], i+ 1, 1, 1, 1)

    def show_window(self):
        self.window.show()

    def update_view(self):
        animals = self.game.herd.common.herd
        for animal, value in animals.items():
            self.common_view_items[animal].setText(str(value))
        for name, view in self.players_view.items():
            animals = self.game.herd.players_herd[name].herd
            for animal, value in animals.items():
                view[animal].setText(str(value))

    def parse_printout(self, to_print):
        return '\n'.join(['{}: {}'.format(k, v) for k, v in to_print.items()])
