from PyQt5 import QtWidgets


class PlayerNamesWindow:
    def __init__(self):
        self.callback = None
        self.window = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout()
        self.radio_buttons = []
        self.players_names = []
        self.name_labels = []
        self.number_of_players = 2
        self.window.setWindowTitle('Farmer Game')

    def setup_main_window(self):
        self.grid_layout.addWidget(QtWidgets.QLabel('Select how many players and enter names:'), 0, 0, 1, 4)
        self.window.setLayout(self.grid_layout)
        self.set_radio_btn_for_players_number()
        self.set_inputs_for_names()
        for i in range(2, 4):
            self.players_names[i].setEnabled(False)
            self.name_labels[i].setEnabled(False)
        self.add_ok_btn()

    def set_radio_btn_for_players_number(self):
        for i in range(3):
            btn = QtWidgets.QRadioButton(str(i + 2))
            btn.toggled.connect(self.number_chage)
            self.radio_buttons.append(btn)
            self.grid_layout.addWidget(btn, 1, i+1, 1, 1)
        self.radio_buttons[0].setChecked(True)

    def set_inputs_for_names(self):
        for i in range(2, 6):
            name_label = QtWidgets.QLabel('Player #{}:'.format(i-1))
            self.name_labels.append(name_label)
            self.grid_layout.addWidget(name_label, i, 0, 1, 1)
            name_input = QtWidgets.QLineEdit()
            self.players_names.append(name_input)
            self.grid_layout.addWidget(name_input, i, 1, 1, 3)

    def number_chage(self):
        if self.window.isActiveWindow():
            btn = self.window.sender()
            number = int(btn.text())
            self.number_of_players = number
            for i in range(4):
                if i >= number:
                    self.players_names[i].setEnabled(False)
                    self.name_labels[i].setEnabled(False)
                else:
                    self.players_names[i].setEnabled(True)
                    self.name_labels[i].setEnabled(True)

    def add_ok_btn(self):
        btn = QtWidgets.QPushButton()
        btn.setText('Play')
        btn.clicked.connect(self.pass_names)
        self.grid_layout.addWidget(btn, 6, 1, 1, 2)

    def pass_names(self):
        players = []
        for i in range(self.number_of_players):
            players.append(self.players_names[i].text())
        if all(players) and len(set(players)) == self.number_of_players:
            self.window.close()
            if self.callback:
                self.callback(players)
        else:
            QtWidgets.QMessageBox.about(self.window, 'Farmer warn', 'enter different names first')

    def set_exit_callback(self, callback):
        self.callback = callback

    def show_window(self):
        self.window.show()



