import subprocess
import json

class Launcher:
    def __init__(self):
        with open("config/emulators.json", "r") as f:
            self.emulators = json.load(f)

    def launch(self, game):
        if game.is_pc:
            cmd = [game.path]
        else:
            emulator = self.emulators.get(game.platform)
            if not emulator:
                raise RuntimeError(f"No emulator for {game.platform}")

            cmd = [emulator["exe"], game.path]

        subprocess.Popen(cmd)
