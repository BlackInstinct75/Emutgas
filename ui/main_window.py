from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from ui.title_bar import TitleBar
from ui.game_grid import GameGrid

class MainWindow(QMainWindow):
    def __init__(self, games, launcher):
        super().__init__()
        self.games = games
        self.launcher = launcher

        self.setWindowTitle("Switch Launcher")
        self.setStyleSheet("background-color: #202020;")

        # Layout principal
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        # Barra superior
        self.title_bar = TitleBar(self)
        layout.addWidget(self.title_bar)

        # Grid de juegos
        self.grid = GameGrid(games)
        layout.addWidget(self.grid)

        self.setCentralWidget(central)
        self.showFullScreen()
