from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class Guard(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.GUARD, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Must stay in palace
        if not target.is_in_palace(self.color):
            return False

        # Move one step diagonally
        row_dist, col_dist = self.current_position.distance_to(target)
        is_one_step_diagonal = row_dist == 1 and col_dist == 1

        if not is_one_step_diagonal:
            return False

        return True
