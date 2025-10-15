from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class Rook(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.ROOK, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Move orthogonally any distance
        row_dist, col_dist = self.current_position.distance_to(target)

        # Must move in straight line (either row or col changes, not both)
        if not (
            (row_dist > 0 and col_dist == 0)
            or (row_dist == 0 and col_dist > 0)
        ):
            return False

        # Path must be clear
        if not board.is_path_clear(self.current_position, target):
            return False

        return True
