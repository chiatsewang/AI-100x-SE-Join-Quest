from typing import Optional
from chess.entities.position import Position, Color


class MoveResult:
    def __init__(
        self,
        is_legal: bool,
        is_game_over: bool = False,
        winner: Optional[Color] = None,
        error_message: Optional[str] = None,
    ):
        self.is_legal = is_legal
        self.is_game_over = is_game_over
        self.winner = winner
        self.error_message = error_message


class Move:
    def __init__(self, piece: "Piece", from_pos: Position, to_pos: Position):
        self.piece = piece
        self.from_pos = from_pos
        self.to_pos = to_pos

    def is_legal(self, board: "Board") -> bool:
        pass

    def execute(self, board: "Board") -> MoveResult:
        pass
