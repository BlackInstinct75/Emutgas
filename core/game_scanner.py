from pathlib import Path
from core.models import Game

class GameScanner:
    EXT_MAP = {
        ".nes": "NES",
        ".sfc": "SNES",
        ".smc": "SNES",
        ".iso": "PS2",
        ".cso": "PSP",
        ".exe": "PC"
    }

    def scan(self, folder: str):
        games = []
        base = Path(folder)

        for file in base.rglob("*"):
            if not file.is_file():
                continue

            ext = file.suffix.lower()
            if ext not in self.EXT_MAP:
                continue

            platform = self.EXT_MAP[ext]

            games.append(
                Game(
                    name=file.stem,
                    path=str(file),
                    platform=platform,
                    cover="assets/covers/default.png",
                    is_pc=(platform == "PC")
                )
            )

        return games
