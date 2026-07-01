from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MoreGamesCard(QWidget):
    """Card para ver más juegos, estilo PS5."""

    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.setStyleSheet("""
            #card {
                background-color: #232326;
                border-radius: 14px;
            }
            QLabel#cardTitle {
                color: #f2f2f2;
                font-size: 14px;
                font-weight: 500;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        cover = QLabel()
        cover.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("assets/generic/games.png")
        if not pixmap.isNull():
            pixmap = pixmap.scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        cover.setPixmap(pixmap)

        title = QLabel("Ver más juegos")
        title.setObjectName("cardTitle")
        title.setAlignment(Qt.AlignCenter)
        title.setWordWrap(True)

        layout.addWidget(cover, 1)
        layout.addWidget(title, 0)
