from typing import Optional
from chess.entities.board import Board
from chess.entities.position import Position, Color, PieceType
from chess.entities.move import MoveResult, Move
from chess.pieces.general import General
from chess.pieces.guard import Guard
from chess.pieces.rook import Rook
from chess.pieces.horse import Horse
from chess.pieces.cannon import Cannon
from chess.pieces.elephant import Elephant
from chess.pieces.soldier import Soldier


class GameService:
    def __init__(self):
        pass

    def create_empty_board(self) -> Board:
        return Board()

    def setup_piece(
        self, board: Board, piece_type: str, color: str, position: tuple
    ):
        # Parse color
        color_enum = Color.RED if color == "Red" else Color.BLACK

        # Create position
        pos = Position(position[0], position[1])

        # Create piece based on type
        if piece_type == "General":
            piece = General(color_enum, pos)
        elif piece_type == "Guard":
            piece = Guard(color_enum, pos)
        elif piece_type == "Rook":
            piece = Rook(color_enum, pos)
        elif piece_type == "Horse":
            piece = Horse(color_enum, pos)
        elif piece_type == "Cannon":
            piece = Cannon(color_enum, pos)
        elif piece_type == "Elephant":
            piece = Elephant(color_enum, pos)
        elif piece_type == "Soldier":
            piece = Soldier(color_enum, pos)
        else:
            raise ValueError(f"Unknown piece type: {piece_type}")

        # Place on board
        board.place_piece(piece, pos)

    def execute_move(
        self, board: Board, from_pos: tuple, to_pos: tuple
    ) -> MoveResult:
        # Get piece at from_pos
        from_position = Position(from_pos[0], from_pos[1])
        to_position = Position(to_pos[0], to_pos[1])

        piece = board.get_piece(from_position)
        if piece is None:
            return MoveResult(
                is_legal=False, error_message="No piece at source position"
            )

        # Check if move is legal
        if not piece.can_move_to(to_position, board):
            return MoveResult(is_legal=False, error_message="Illegal move")

        # Check if this is a capture
        captured_piece = board.get_piece(to_position)

        # Execute move
        board.remove_piece(from_position)
        board.place_piece(piece, to_position)
        piece.current_position = to_position

        # Check if captured opponent's General (win condition)
        if captured_piece and captured_piece.get_type() == PieceType.GENERAL:
            return MoveResult(
                is_legal=True, is_game_over=True, winner=piece.get_color()
            )

        return MoveResult(is_legal=True)
