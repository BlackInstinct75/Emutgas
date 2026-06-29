from PySide6.QtWidgets import QWidget, QGridLayout
from ui.game_card import GameCard
from ui.empty_card import EmptyCard

class GameGrid(QWidget):
    def __init__(self, games):
        super().__init__()
        layout = QGridLayout(self)

        # Número de huecos estilo Switch
        TOTAL_SLOTS = 12

        # Si no hay juegos, rellenar con huecos vacíos
        if not games:
            for i in range(TOTAL_SLOTS):
                layout.addWidget(EmptyCard(), i // 6, i % 6)
            return

        # Si hay juegos, dibujar juegos + huecos
        row = col = 0
        for game in games:
            layout.addWidget(GameCard(game), row, col)
            col += 1
            if col >= 6:
                col = 0
                row += 1

        # Rellenar huecos restantes
        used = len(games)
        for i in range(used, TOTAL_SLOTS):
            layout.addWidget(EmptyCard(), i // 6, i % 6)
