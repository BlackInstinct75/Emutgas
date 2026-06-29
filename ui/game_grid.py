from PySide6.QtWidgets import QWidget, QGridLayout
from ui.game_card import GameCard
from ui.store_card import StoreCard
from ui.more_games_card import MoreGamesCard
from ui.empty_card import EmptyCard

"""
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
"""
class GameGrid(QWidget):
    def __init__(self, games):
        super().__init__()

        layout = QGridLayout(self)
        layout.setSpacing(20)

        row = 0
        col = 0

        # 1. Card de Tienda SIEMPRE primero
        layout.addWidget(StoreCard(), row, col)
        col += 1

        # 2. Si no hay juegos → card vacía
        if not games:
            layout.addWidget(EmptyCard(), row, col)
            col += 1
        else:
            # 3. Cards de juegos
            for game in games:
                layout.addWidget(GameCard(game), row, col)
                col += 1
                if col >= 4:
                    col = 0
                    row += 1

        # 4. Card “Ver más juegos” SIEMPRE al final
        if col >= 4:
            col = 0
            row += 1
    
        layout.addWidget(MoreGamesCard(), row, col)
