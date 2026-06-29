from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class MoreGamesCard(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("moreGamesCard")
        self.setStyleSheet("""
            #moreGamesCard {
                border: 2px solid #333;
                border-radius: 10px;
                background-color: #222;
                padding: 10px;
            }
        """)

        layout = QVBoxLayout(self)

        cover = QLabel()
        cover.setPixmap(QPixmap("assets/generic/games.png").scaled(200, 200))

        title = QLabel("Ver más juegos")
        title.setStyleSheet("color: white; font-size: 18px;")

        layout.addWidget(cover)
        layout.addWidget(title)
