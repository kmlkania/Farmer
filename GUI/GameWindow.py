from PyQt5 import QtWidgets
from Game import Game
from GUI.ExchangeWindow import ExchangeWindow


class GameWindow:
    def __init__(self, players):
        self.window = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout()
        self.window.setLayout(self.grid_layout)
        self.players_names = players
        self.game = Game(players)
        self.common_view_items = {}
        self.players_view = {}
        self.info_viewer = None

    def setup_window(self):
        self.window.setWindowTitle('Farmer Game')
        self.configure_common_widget()
        self.configure_player_widget()
        self.configure_info_widget()
        self.update_view()
        self.set_game_callbacks()
        self.update_info("{} starts the game".format(self.players_names[0]))

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
            self.add_action_buttons(widget=inside_grid, name=name)
            if i > 0:
                self.players_view[name]['roll'].setEnabled(False)
                self.players_view[name]['exchange'].setEnabled(False)

    def configure_info_widget(self):
        info_widget = QtWidgets.QWidget()
        self.grid_layout.addWidget(info_widget, 2, 0, 1, len(self.players_names))
        self.info_viewer = QtWidgets.QTextBrowser()
        inside_grid = QtWidgets.QGridLayout()
        info_widget.setLayout(inside_grid)
        inside_grid.addWidget(self.info_viewer, 0, 0, 1, 1)
        self.info_viewer.append('game start')

    def add_action_buttons(self, widget, name):
        roll_btn = QtWidgets.QPushButton()
        roll_btn.setText('Roll')
        widget.addWidget(roll_btn, 8, 0, 1, 1)
        exchange_btn = QtWidgets.QPushButton()
        exchange_btn.setText('Change')
        widget.addWidget(exchange_btn, 8, 1, 1, 1)
        roll_btn.clicked.connect(self.make_user_roll(name))
        exchange_btn.clicked.connect(self.make_user_exchange(name))
        self.players_view[name].update({'roll': roll_btn, 'exchange': exchange_btn})

    def make_user_roll(self, name):
        def user_roll():
            self.game.make_roll(name)
        return user_roll

    def make_user_exchange(self, name):
        def user_exchange():
            self.make_exchange(name)
        return user_exchange

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

    def set_game_callbacks(self):
        self.game.set_info_callback(self.update_info)
        self.game.set_end_turn_callback(self.change_active_player)

    def update_info(self, msg):
        self.info_viewer.append(msg)

    def change_active_player(self, current_player_name):
        index_of_next_player = (self.players_names.index(current_player_name) + 1) % len(self.players_names)
        for i, name in enumerate(self.players_names):
            if i == index_of_next_player:
                self.players_view[name]['roll'].setEnabled(True)
                self.players_view[name]['exchange'].setEnabled(True)
                self.update_info("{}'s turn".format(name))
            else:
                self.players_view[name]['roll'].setEnabled(False)
                self.players_view[name]['exchange'].setEnabled(False)
        self.update_view()

    def make_exchange(self, name):
        exchange_window = ExchangeWindow()
        exchange_window.set_exchange_callback(self.animals_exchanged)
        exchange_window.setup_window(name, self.game.herd.players_herd[name].herd)
        result = exchange_window.show_window()

    def animals_exchanged(self, name, animals_to_sell, animals_to_buy):
        self.game.sell_animals(name, animals_to_sell)
        self.game.buy_animals(name, animals_to_buy)
        self.update_view()

