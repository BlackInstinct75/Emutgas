from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
from ui.game_grid import GameGrid
from ui.TopRightBar import TopRightBar

class MainWindow(QMainWindow):
    def __init__(self, games, launcher):
        super().__init__()
        self.games = games
        self.launcher = launcher

        self.setWindowTitle("Emugast")
        self.setWindowIcon(QIcon("assets/generic/logo.jpeg"))

        # Aplicar tema
        # self.apply_theme("dark")
        self.apply_theme("light")

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        top_right_bar = TopRightBar()
        layout.addWidget(top_right_bar)
        
        self.grid = GameGrid(games)
        layout.addWidget(self.grid)

        self.setCentralWidget(central)
        self.showFullScreen()

    def apply_theme(self, name):
        with open(f"themes/{name}.qss", "r") as f:
            self.setStyleSheet(f.read())
