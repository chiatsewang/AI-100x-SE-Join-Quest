from chess.entities.piece import Piece
from chess.entities.position import Color, PieceType, Position


class Cannon(Piece):
    def __init__(self, color: Color, current_position: Position):
        super().__init__(color, PieceType.CANNON, current_position)

    def can_move_to(self, target: Position, board: "Board") -> bool:
        # Move orthogonally like a Rook
        row_dist, col_dist = self.current_position.distance_to(target)

        # Must move in straight line
        if not (
            (row_dist > 0 and col_dist == 0)
            or (row_dist == 0 and col_dist > 0)
        ):
            return False

        # Count pieces between current position and target
        pieces_count = board.count_pieces_between(
            self.current_position, target
        )

        # Check if target is occupied
        target_piece = board.get_piece(target)
        is_capture = target_piece is not None

        if is_capture:
            # Must jump exactly one piece to capture
            if pieces_count != 1:
                return False
        else:
            # Path must be clear when not capturing
            if pieces_count != 0:
                return False

        return True
