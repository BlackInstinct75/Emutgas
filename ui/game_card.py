from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class GameCard(QWidget):
    """Card de un juego: portada + título, estilo PS5."""

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.setObjectName("card")

        # --- SIN FONDO, TOTALMENTE TRANSPARENTE ---
        self.setStyleSheet("""
            #card {
                background: transparent;
            }
            QLabel#cardTitle {
                color: white;
                font-size: 14px;
                font-weight: 500;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        self.cover = QLabel()
        self.cover.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(self.game.cover)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.cover.setPixmap(pixmap)
        self.cover.setObjectName("cardCover")

        self.title = QLabel(self.game.name)
        self.title.setObjectName("cardTitle")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)

        layout.addWidget(self.cover, 1)
        layout.addWidget(self.title, 0)

