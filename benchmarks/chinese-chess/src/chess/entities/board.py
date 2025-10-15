from typing import Optional, Dict
from chess.entities.position import Position, PieceType, Color


class Board:
    def __init__(self):
        self.pieces: Dict[tuple, "Piece"] = {}

    def place_piece(self, piece: "Piece", position: Position):
        key = (position.row, position.col)
        self.pieces[key] = piece

    def get_piece(self, position: Position) -> Optional["Piece"]:
        key = (position.row, position.col)
        return self.pieces.get(key)

    def is_empty(self, position: Position) -> bool:
        return self.get_piece(position) is None

    def remove_piece(self, position: Position) -> Optional["Piece"]:
        key = (position.row, position.col)
        return self.pieces.pop(key, None)

    def find_general(self, color: Color) -> Optional[Position]:
        """Find the position of the General for the given color."""
        for (row, col), piece in self.pieces.items():
            if (
                piece.get_type() == PieceType.GENERAL
                and piece.get_color() == color
            ):
                return Position(row, col)
        return None

    def are_generals_facing(self) -> bool:
        """Check if the two Generals are facing each other on the same column."""
        red_general_pos = self.find_general(Color.RED)
        black_general_pos = self.find_general(Color.BLACK)

        if not red_general_pos or not black_general_pos:
            return False

        # Check if they're on the same column
        if red_general_pos.col != black_general_pos.col:
            return False

        # Check if there are any pieces between them
        min_row = min(red_general_pos.row, black_general_pos.row)
        max_row = max(red_general_pos.row, black_general_pos.row)

        for row in range(min_row + 1, max_row):
            pos = Position(row, red_general_pos.col)
            if not self.is_empty(pos):
                return False

        return True

    def is_path_clear(self, from_pos: Position, to_pos: Position) -> bool:
        """Check if the path between two positions is clear (no pieces blocking)."""
        row_diff = to_pos.row - from_pos.row
        col_diff = to_pos.col - from_pos.col

        # Determine direction
        row_step = 0 if row_diff == 0 else (1 if row_diff > 0 else -1)
        col_step = 0 if col_diff == 0 else (1 if col_diff > 0 else -1)

        # Check each position along the path (excluding start and end)
        current_row = from_pos.row + row_step
        current_col = from_pos.col + col_step

        while current_row != to_pos.row or current_col != to_pos.col:
            pos = Position(current_row, current_col)
            if not self.is_empty(pos):
                return False
            current_row += row_step
            current_col += col_step

        return True

    def count_pieces_between(
        self, from_pos: Position, to_pos: Position
    ) -> int:
        """Count the number of pieces between two positions (excluding start and end)."""
        row_diff = to_pos.row - from_pos.row
        col_diff = to_pos.col - from_pos.col

        # Determine direction
        row_step = 0 if row_diff == 0 else (1 if row_diff > 0 else -1)
        col_step = 0 if col_diff == 0 else (1 if col_diff > 0 else -1)

        # Count pieces along the path
        count = 0
        current_row = from_pos.row + row_step
        current_col = from_pos.col + col_step

        while current_row != to_pos.row or current_col != to_pos.col:
            pos = Position(current_row, current_col)
            if not self.is_empty(pos):
                count += 1
            current_row += row_step
            current_col += col_step

        return count
