from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class EmptyCard(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("card")  # usa el estilo del tema

        layout = QVBoxLayout(self)

        # Bloque de color (sin imagen)
        color_block = QWidget()
        color_block.setFixedSize(150, 150)
        color_block.setObjectName("emptyBlock")

        title = QLabel("Vacío")
        title.setObjectName("title")

        layout.addWidget(color_block)
        layout.addWidget(title)

