from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

class GameCard(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game

        layout = QVBoxLayout(self)
        self.cover = QLabel()
        self.cover.setPixmap(QPixmap(game.cover).scaled(200, 200))

        self.title = QLabel(game.name)
        self.title.setStyleSheet("color: white; font-size: 18px;")

        layout.addWidget(self.cover)
        layout.addWidget(self.title)
