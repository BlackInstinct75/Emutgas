from dataclasses import dataclass

@dataclass
class Game:
    name: str
    path: str
    platform: str
    cover: str
    is_pc: bool = False
