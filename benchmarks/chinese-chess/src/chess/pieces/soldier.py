from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class Soldier(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.SOLDIER, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Move one step only
        row_dist, col_dist = self.current_position.distance_to(target)

        if row_dist + col_dist != 1:
            return False

        # Determine if soldier has crossed the river
        has_crossed_river = False
        if self.color == Color.RED:
            # Red soldier crosses river at row 6
            has_crossed_river = self.current_position.row >= 6
            # Cannot move backward (row must increase or stay same)
            if target.row < self.current_position.row:
                return False
            # Before crossing, can only move forward (no sideways)
            if not has_crossed_river and col_dist != 0:
                return False
        else:
            # Black soldier crosses river at row 5
            has_crossed_river = self.current_position.row <= 5
            # Cannot move backward (row must decrease or stay same)
            if target.row > self.current_position.row:
                return False
            # Before crossing, can only move forward (no sideways)
            if not has_crossed_river and col_dist != 0:
                return False

        return True
