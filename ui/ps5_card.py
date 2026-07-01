from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class CardSlot(QWidget):
    """
    Contenedor al estilo PS5.

    Reserva un hueco fijo dentro de la fila horizontal (para que las demás
    cards no se muevan), pero por dentro coloca la card "libre" (sin
    layout) para poder animarla: al pasar el ratón por encima, o al
    seleccionarla con las flechas del teclado, la card crece suavemente
    y se resalta con un resplandor, tal como en el menú principal de
    PlayStation 5.
    """

    NORMAL_SIZE = (190, 230)
    HOVER_SCALE = 1.16
    ANIM_MS = 180

    def __init__(self, card_widget, index=0, on_hover=None):
        super().__init__()
        self.index = index
        self._on_hover = on_hover
        self._active = False

        nw, nh = self.NORMAL_SIZE
        # El slot reserva algo más de hueco del tamaño normal, para dejar
        # aire a la animación de crecimiento sin que las cards vecinas
        # se solapen demasiado.
        self.setFixedSize(int(nw * 1.05), int(nh * 1.05))
        self.setAttribute(Qt.WA_Hover, True)

        self.card = card_widget
        self.card.setParent(self)
        self.card.setGeometry(self._normal_rect())

        # Resplandor que aparece al activar la card
        self.glow = QGraphicsDropShadowEffect(self.card)
        self.glow.setBlurRadius(0)
        self.glow.setOffset(0, 0)
        self.glow.setColor(QColor(0, 174, 255, 220))
        self.card.setGraphicsEffect(self.glow)

        self.anim = QPropertyAnimation(self.card, b"geometry")
        self.anim.setDuration(self.ANIM_MS)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)

        self.glow_anim = QPropertyAnimation(self.glow, b"blurRadius")
        self.glow_anim.setDuration(self.ANIM_MS)

    # ---- geometría ----

    def _normal_rect(self):
        nw, nh = self.NORMAL_SIZE
        x = (self.width() - nw) // 2
        y = (self.height() - nh) // 2
        return QRect(x, y, nw, nh)

    def _hover_rect(self):
        nw, nh = self.NORMAL_SIZE
        hw, hh = int(nw * self.HOVER_SCALE), int(nh * self.HOVER_SCALE)
        x = (self.width() - hw) // 2
        y = (self.height() - hh) // 2
        return QRect(x, y, hw, hh)

    def _animate_to(self, rect, blur):
        self.anim.stop()
        self.anim.setStartValue(self.card.geometry())
        self.anim.setEndValue(rect)
        self.anim.start()

        self.glow_anim.stop()
        self.glow_anim.setStartValue(self.glow.blurRadius())
        self.glow_anim.setEndValue(blur)
        self.glow_anim.start()

    # ---- estado ----

    def set_active(self, active: bool):
        if self._active == active:
            return
        self._active = active
        if active:
            self.raise_()  # que quede por encima de las cards vecinas
            self._animate_to(self._hover_rect(), 34)
        else:
            self._animate_to(self._normal_rect(), 0)

    def is_active(self):
        return self._active

    # ---- ratón ----

    def enterEvent(self, event):
        if self._on_hover:
            self._on_hover(self.index)
        super().enterEvent(event)
