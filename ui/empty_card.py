from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

class EmptyCard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        cover = QLabel()
        cover.setPixmap(QPixmap("assets/covers/empty.png").scaled(200, 200))

        title = QLabel("Vacío")
        title.setStyleSheet("color: gray; font-size: 16px;")

        layout.addWidget(cover)
        layout.addWidget(title)
