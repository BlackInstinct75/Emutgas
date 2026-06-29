from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

class StoreCard(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("storeCard")
        self.setStyleSheet("""
            #storeCard {
                border: 2px solid #222;
                border-radius: 10px;
                background-color: #111;
                padding: 10px;
            }
        """)

        layout = QVBoxLayout(self)

        cover = QLabel()
        cover.setPixmap(QPixmap("assets/generic/store.png").scaled(200, 200))
        cover.setObjectName("storeCover")

        title = QLabel("Tienda")
        title.setStyleSheet("color: white; font-size: 18px;")

        layout.addWidget(cover)
        layout.addWidget(title)
