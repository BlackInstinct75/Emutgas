from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class StoreCard(QWidget):
    """Card de acceso a la tienda, estilo PS5."""

    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.setStyleSheet("""
            #card {
                background-color: #0d2b45;
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
        pixmap = QPixmap("assets/generic/store.png")
        if not pixmap.isNull():
            pixmap = pixmap.scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        cover.setPixmap(pixmap)
        cover.setObjectName("storeCover")

        title = QLabel("Tienda")
        title.setObjectName("cardTitle")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(cover, 1)
        layout.addWidget(title, 0)
