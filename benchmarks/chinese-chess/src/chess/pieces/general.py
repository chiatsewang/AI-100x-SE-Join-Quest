from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class General(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.GENERAL, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Must stay in palace
        if not target.is_in_palace(self.color):
            return False

        # Move one step orthogonally
        row_dist, col_dist = self.current_position.distance_to(target)
        is_one_step_orthogonal = (row_dist == 1 and col_dist == 0) or (
            row_dist == 0 and col_dist == 1
        )
        if not is_one_step_orthogonal:
            return False

        # Check if this move would cause Generals to face each other
        # We need to simulate the move temporarily
        old_pos_key = (self.current_position.row, self.current_position.col)
        new_pos_key = (target.row, target.col)

        # Temporarily make the move on the board
        board.pieces.pop(old_pos_key, None)
        board.pieces[new_pos_key] = self

        # Check if Generals are facing
        facing = board.are_generals_facing()

        # Restore the board state
        board.pieces.pop(new_pos_key, None)
        board.pieces[old_pos_key] = self

        if facing:
            return False

        return True
