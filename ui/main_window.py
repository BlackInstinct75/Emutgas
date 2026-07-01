from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QSizePolicy
from PySide6.QtGui import QIcon, QPainter, QImage
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoSink
from PySide6.QtCore import QUrl, Qt

from ui.game_grid import GameGrid
from ui.TopRightBar import TopRightBar

class VideoBackgroundWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.current_frame = QImage()
        self.sink = QVideoSink()
        self.sink.videoFrameChanged.connect(self.process_frame)

    def process_frame(self, frame):
        self.current_frame = frame.toImage()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.current_frame.isNull():
            painter.drawImage(self.rect(), self.current_frame)
        else:
            painter.fillRect(self.rect(), Qt.black)

class MainWindow(QMainWindow):
    def __init__(self, games, launcher):
        super().__init__()
        self.games = games
        self.launcher = launcher

        self.setWindowTitle("Emugast")
        self.setWindowIcon(QIcon("assets/generic/logo.png"))

        central = QWidget()
        self.setCentralWidget(central)

        layout = QStackedLayout(central)
        layout.setStackingMode(QStackedLayout.StackAll)

        self.video_bg = VideoBackgroundWidget()
        layout.addWidget(self.video_bg)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_bg.sink)

        audio = QAudioOutput()
        audio.setVolume(0.0)
        self.player.setAudioOutput(audio)

        self.player.setSource(QUrl.fromLocalFile("assets/generic/wallpaper.mp4"))
        self.player.play()
        self.player.mediaStatusChanged.connect(self.restart_video)

        # --- CAPA DE LA UI MODIFICADA ---
        ui_layer = QWidget()
        ui_layout = QVBoxLayout(ui_layer)
        ui_layout.setContentsMargins(0, 0, 0, 0)
        
        # CAMBIO 1: Controla la distancia de separación entre la barra y el grid (en píxeles)
        ui_layout.setSpacing(10) 

        top_right_bar = TopRightBar()
        ui_layout.addWidget(top_right_bar)

        self.grid = GameGrid(games)
        ui_layout.addWidget(self.grid)

        # CAMBIO 2: Añadimos un espaciador elástico al final
        # Esto empuja la barra y el grid hacia arriba, pegándolos al tope superior
        ui_layout.addStretch()

        layout.addWidget(ui_layer)
        ui_layer.raise_()

        self.showFullScreen()
        self.grid.setFocus()

    def restart_video(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()