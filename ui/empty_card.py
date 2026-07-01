from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class EmptyCard(QWidget):
    """Hueco vacío, estilo PS5 (placeholder discreto para instalar un juego)."""

    def __init__(self):
        super().__init__()
        self.setObjectName("card")

        # --- SIN FONDO, TRANSPARENTE ---
        self.setStyleSheet("""
            #card {
                background: transparent;
                border: 2px dashed #3a3a3d;
                border-radius: 14px;
            }
            QLabel#emptyIcon {
                color: #55565a;
                font-size: 46px;
            }
            QLabel#cardTitle {
                color: #8a8b8f;
                font-size: 14px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignCenter)

        icon = QLabel("+")
        icon.setObjectName("emptyIcon")
        icon.setAlignment(Qt.AlignCenter)

        title = QLabel("Vacío")
        title.setObjectName("cardTitle")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(icon, 1)
        layout.addWidget(title, 0)
