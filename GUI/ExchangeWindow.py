from PyQt5 import QtWidgets


PRICE_LIST = {
    'rabbit': 1,
    'sheep': 6,
    'pig': 12,
    'cow': 36,
    'horse': 72,
    'small_dog': 6,
    'big_dog': 36
}


class ExchangeWindow:
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        self.grid_layout = QtWidgets.QGridLayout()
        self.dialog.setLayout(self.grid_layout)
        self.spin_boxes = {'sell': {}, 'buy': {}}
        self.available_animals = {}
        self.exchange_callback = None
        self.player_name = ''

    def setup_window(self, name, animals):
        self.player_name = name
        self.available_animals = animals
        for i, text in enumerate(['Animal', 'Your Herd', 'Sell', 'Buy']):
            self.grid_layout.addWidget(QtWidgets.QLabel(text), 0, i, 1, 1)
        offset = 1
        for i, animal in enumerate(animals.items()):
            self.grid_layout.addWidget(QtWidgets.QLabel(animal[0]), offset + i, 0, 1, 1)
            self.grid_layout.addWidget(QtWidgets.QLabel(str(animal[1])), offset + i, 1, 1, 1)
            sell_spin_box = QtWidgets.QSpinBox()
            buy_spin_box = QtWidgets.QSpinBox()
            self.spin_boxes['sell'].update({animal[0]: sell_spin_box})
            self.spin_boxes['buy'].update({animal[0]: buy_spin_box})
            self.grid_layout.addWidget(sell_spin_box, offset + i, 2, 1, 1)
            self.grid_layout.addWidget(buy_spin_box, offset + i, 3, 1, 1)
        offset += len(animals)
        ok_btn = QtWidgets.QPushButton()
        ok_btn.setText('OK')
        self.grid_layout.addWidget(ok_btn, offset, 1, 1, 1)
        cancel_btn = QtWidgets.QPushButton()
        cancel_btn.setText('cancel')
        self.grid_layout.addWidget(cancel_btn, offset, 2, 1, 1)
        ok_btn.clicked.connect(self.exchange_animals)

    def exchange_animals(self):
        animals_to_sell = {animal: number.value() for animal, number in self.spin_boxes['sell'].items() if number.value()}
        animals_to_buy = {animal: number.value() for animal, number in self.spin_boxes['buy'].items() if number.value()}
        if self.exchange_possible(animals_to_sell, animals_to_buy):
            self.exchange_callback(self.player_name, animals_to_sell, animals_to_buy)
            self.dialog.done(0)

    def exchange_possible(self, animals_to_sell, animals_to_buy):
        animals_available = self.player_has_enough_animals(animals_to_sell)
        buy_equals_sell = self.check_if_buy_equals_sell(animals_to_sell, animals_to_buy)
        return animals_available and buy_equals_sell

    def player_has_enough_animals(self, animals_to_sell):
        result = True
        for animal, value in animals_to_sell.items():
            result = result and (self.available_animals[animal] >= value)
        return result

    @staticmethod
    def check_if_buy_equals_sell(animals_to_sell, animals_to_buy):
        sell = 0
        buy = 0
        for animal, value in animals_to_sell.items():
            sell += PRICE_LIST[animal] * value
        for animal, value in animals_to_buy.items():
            buy += PRICE_LIST[animal] * value
        return sell == buy

    def set_exchange_callback(self, callback):
        self.exchange_callback = callback

    def show_window(self):
        return self.dialog.exec()
