from abc import ABC, abstractmethod
from chess.entities.position import Color, PieceType, Position


class Piece(ABC):
    def __init__(
        self, color: Color, piece_type: PieceType, current_position: Position
    ):
        self.color = color
        self.piece_type = piece_type
        self.current_position = current_position

    @abstractmethod
    def can_move_to(self, target: Position, board) -> bool:
        pass

    def get_color(self) -> Color:
        return self.color

    def get_type(self) -> PieceType:
        return self.piece_type
