from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class Horse(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.HORSE, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Move in "L" shape (2 steps in one direction, 1 step perpendicular)
        row_dist, col_dist = self.current_position.distance_to(target)

        # Check if it's a valid L-shape
        is_l_shape = (row_dist == 2 and col_dist == 1) or (
            row_dist == 1 and col_dist == 2
        )
        if not is_l_shape:
            return False

        # Check for blocking piece at intermediate position (leg-block)
        # The blocking position is one step in the direction of the longer move
        if row_dist == 2:
            # Moving 2 steps vertically, check the position 1 step away
            block_row = (
                self.current_position.row + 1
                if target.row > self.current_position.row
                else self.current_position.row - 1
            )
            block_pos = Position(block_row, self.current_position.col)
        else:
            # Moving 2 steps horizontally, check the position 1 step away
            block_col = (
                self.current_position.col + 1
                if target.col > self.current_position.col
                else self.current_position.col - 1
            )
            block_pos = Position(self.current_position.row, block_col)

        if not board.is_empty(block_pos):
            return False

        return True
