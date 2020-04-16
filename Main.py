from PyQt5.QtWidgets import QApplication
import sys
from GUI.WindowHandler import WindowHandler


def start_app():
    app = QApplication(sys.argv)
    game_window = WindowHandler()
    game_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_app()
