from PySide6.QtWidgets import QApplication
from core.game_scanner import GameScanner
from core.launcher import Launcher
from ui.main_window import MainWindow
import sys

def main():
    app = QApplication(sys.argv)

    scanner = GameScanner()
    games = scanner.scan("roms/")

    launcher = Launcher()

    window = MainWindow(games, launcher)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
