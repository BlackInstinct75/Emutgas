from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class TitleBar(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        # Botón minimizar
        self.min_btn = QPushButton("—")
        self.min_btn.setFixedSize(40, 30)
        self.min_btn.clicked.connect(self.minimize)

        # Botón maximizar/restaurar
        self.max_btn = QPushButton("⬜")
        self.max_btn.setFixedSize(40, 30)
        self.max_btn.clicked.connect(self.maximize_restore)

        # Botón cerrar
        self.close_btn = QPushButton("X")
        self.close_btn.setFixedSize(40, 30)
        self.close_btn.clicked.connect(self.close_window)

        layout.addWidget(self.min_btn)
        layout.addWidget(self.max_btn)
        layout.addWidget(self.close_btn)

        self.setStyleSheet("""
            QPushButton {
                background-color: #333;
                color: white;
                border: none;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

    def minimize(self):
        self.window.showMinimized()

    def maximize_restore(self):
        if self.window.isMaximized():
            self.window.showNormal()
        else:
            self.window.showMaximized()

    def close_window(self):
        self.window.close()
