from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class Elephant(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.ELEPHANT, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Move 2 steps diagonally
        row_dist, col_dist = self.current_position.distance_to(target)

        if row_dist != 2 or col_dist != 2:
            return False

        # Cannot cross river (row 5 and 6 are river boundary)
        if self.color == Color.RED:
            # Red elephant must stay in rows 1-5
            if target.row > 5:
                return False
        else:
            # Black elephant must stay in rows 6-10
            if target.row < 6:
                return False

        # Check if midpoint is blocked
        mid_row = (self.current_position.row + target.row) // 2
        mid_col = (self.current_position.col + target.col) // 2
        mid_pos = Position(mid_row, mid_col)

        if not board.is_empty(mid_pos):
            return False

        return True
