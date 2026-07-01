from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
import pytz
from datetime import datetime

class TopRightBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("topRightBar")
        self.setFixedHeight(80)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(20)

        # --- ESPACIADOR PARA EMPUJAR TODO A LA DERECHA ---
        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer)

        # --- Reloj ---
        self.clock = QLabel()
        self.clock.setObjectName("clock")
        self.clock.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        tz = pytz.timezone("Europe/Madrid")
        self.tz = tz

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

        # --- Icono de usuario ---
        self.user_icon = QLabel()
        self.user_icon.setObjectName("userIcon")
        self.user_icon.setPixmap(QPixmap("assets/generic/user.png").scaled(32, 32, Qt.KeepAspectRatio))

        # --- Icono de configuración ---
        self.settings_icon = QLabel()
        self.settings_icon.setObjectName("settingsIcon")
        self.settings_icon.setPixmap(QPixmap("assets/generic/settings.png").scaled(32, 32, Qt.KeepAspectRatio))

        # Añadir widgets al layout (ya están empujados a la derecha)
        
        layout.addWidget(self.settings_icon)
        layout.addWidget(self.user_icon)
        layout.addWidget(self.clock)

    def update_time(self):
        now = datetime.now(self.tz)
        self.clock.setText(now.strftime("%H:%M"))