from PySide6.QtWidgets import QWidget, QHBoxLayout, QScrollArea, QSizePolicy
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve

from ui.game_card import GameCard
from ui.store_card import StoreCard
from ui.more_games_card import MoreGamesCard
from ui.empty_card import EmptyCard
from ui.ps5_card import CardSlot


class GameGrid(QScrollArea):
    """
    Fila horizontal de cards al estilo del menú principal de PS5.
    """

    def __init__(self, games):
        super().__init__()

        # --- ELIMINAR FONDO DEL SCROLLAREA ---
        self.setStyleSheet("background: transparent; border: none;")
        self.setFixedHeight(200)
        self.setObjectName("gameGrid")
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QScrollArea.NoFrame)
        self.setFocusPolicy(Qt.StrongFocus)

        # --- CONTENEDOR INTERNO ---
        content = QWidget()
        content.setObjectName("gameGridContent")
        content.setStyleSheet("background: transparent;")
        content.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        self.row = QHBoxLayout(content)

        # 🔥 AJUSTE CLAVE: GameGrid más arriba
        self.row.setContentsMargins(50, 10, 50, 20)
        self.row.setSpacing(28)
        self.row.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.setWidget(content)
        self.content = content

        self.slots = []
        self._build_slots(games)

        self.current_index = 0
        if self.slots:
            self.slots[0].set_active(True)

        self._scroll_anim = QPropertyAnimation(self.horizontalScrollBar(), b"value")
        self._scroll_anim.setDuration(260)
        self._scroll_anim.setEasingCurve(QEasingCurve.OutCubic)

    # ---- construcción ----

    def _add_slot(self, widget):
        index = len(self.slots)

        slot = CardSlot(widget, index=index, on_hover=self._on_hover)
        slot.setStyleSheet("background: transparent;")

        self.row.addWidget(slot)
        self.slots.append(slot)

        widget.setStyleSheet("background: transparent;")

    def _build_slots(self, games):
        self._add_slot(StoreCard())

        if not games:
            self._add_slot(EmptyCard())
        else:
            for game in games:
                self._add_slot(GameCard(game))

        self._add_slot(MoreGamesCard())

    # ---- selección / navegación ----

    def _select(self, index):
        if not self.slots:
            return
        index = max(0, min(index, len(self.slots) - 1))
        if index == self.current_index:
            return
        self.slots[self.current_index].set_active(False)
        self.current_index = index
        self.slots[index].set_active(True)
        self._scroll_to(index)

    def _on_hover(self, index):
        self._select(index)

    def _scroll_to(self, index):
        slot = self.slots[index]
        target_center = slot.x() + slot.width() / 2
        viewport_width = self.viewport().width()
        target_value = int(target_center - viewport_width / 2)

        bar = self.horizontalScrollBar()
        target_value = max(bar.minimum(), min(target_value, bar.maximum()))

        self._scroll_anim.stop()
        self._scroll_anim.setStartValue(bar.value())
        self._scroll_anim.setEndValue(target_value)
        self._scroll_anim.start()

    # ---- teclado ----

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Right, Qt.Key_D):
            self._select(self.current_index + 1)
        elif event.key() in (Qt.Key_Left, Qt.Key_A):
            self._select(self.current_index - 1)
        else:
            super().keyPressEvent(event)

    # ---- rueda del ratón ----

    def wheelEvent(self, event):
        delta = event.angleDelta().y() or event.angleDelta().x()
        if delta < 0:
            self._select(self.current_index + 1)
        elif delta > 0:
            self._select(self.current_index - 1)
        event.accept()
