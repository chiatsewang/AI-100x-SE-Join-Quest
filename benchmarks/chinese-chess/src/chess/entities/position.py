from enum import Enum


class Color(Enum):
    RED = "Red"
    BLACK = "Black"


class PieceType(Enum):
    GENERAL = "General"
    GUARD = "Guard"
    ROOK = "Rook"
    HORSE = "Horse"
    CANNON = "Cannon"
    ELEPHANT = "Elephant"
    SOLDIER = "Soldier"


class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def is_valid(self) -> bool:
        return 1 <= self.row <= 10 and 1 <= self.col <= 9

    def is_in_palace(self, color: Color) -> bool:
        if not (4 <= self.col <= 6):
            return False
        if color == Color.RED:
            return 1 <= self.row <= 3
        else:  # BLACK
            return 8 <= self.row <= 10

    def distance_to(self, other: "Position") -> tuple:
        return abs(self.row - other.row), abs(self.col - other.col)
