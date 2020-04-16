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
        self.grid_layout.addWidget(common_widget, 0, 0, 1, 1)
        inside_grid = QtWidgets.QGridLayout()
        common_widget.setLayout(inside_grid)
        self.fill_herd_owner(name='common herd', widget=inside_grid)
        animals = self.game.herd.common.herd
        self.common_view_items = {animal: QtWidgets.QLabel(common_widget) for animal in animals.keys()}
        self.fill_herd_view(herd=self.common_view_items, widget=inside_grid)

    def configure_player_widget(self):
        for i, name in enumerate(self.players_names):
            player_widget = QtWidgets.QWidget()
            self.grid_layout.addWidget(player_widget, 1, i, 1, 1)
            inside_grid = QtWidgets.QGridLayout()
            player_widget.setLayout(inside_grid)
            self.fill_herd_owner(name=name, widget=inside_grid)
            animals = self.game.herd.players_herd[name].herd
            self.players_view.update({name: {animal: QtWidgets.QLabel() for animal in animals.keys()}})
            self.fill_herd_view(herd=self.players_view[name], widget=inside_grid)
            self.add_action_buttons(widget=inside_grid)

    @staticmethod
    def add_action_buttons(widget):
        roll_btn = QtWidgets.QPushButton()
        roll_btn.setText('Roll')
        roll_btn.clicked.connect(lambda x: None)
        widget.addWidget(roll_btn, 8, 0, 1, 1)
        roll_btn = QtWidgets.QPushButton()
        roll_btn.setText('Change')
        roll_btn.clicked.connect(lambda x: None)
        widget.addWidget(roll_btn, 8, 1, 1, 1)

    @staticmethod
    def fill_herd_owner(name, widget):
        lbl = QtWidgets.QLabel()
        lbl.setText(name)
        widget.addWidget(lbl, 0, 0, 1, 2)

    @staticmethod
    def fill_herd_view(herd, widget):
        for i, item in enumerate(herd.items()):
            lbl = QtWidgets.QLabel()
            lbl.setText(item[0])
            widget.addWidget(lbl, i+ 1, 0, 1, 1)
            widget.addWidget(item[1], i+ 1, 1, 1, 1)

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
