from behave import given, when, then
from chess.game.game_service import GameService


@given("the board is empty except for a {color} {piece_type} at {position}")
def step_setup_single_piece(context, color, piece_type, position):
    context.game_service = GameService()
    context.board = context.game_service.create_empty_board()
    context.game_service.setup_piece(
        context.board, piece_type, color, eval(position)
    )


@given("the board has:")
def step_setup_multiple_pieces(context):
    context.game_service = GameService()
    context.board = context.game_service.create_empty_board()
    for row in context.table:
        piece_str = row["Piece"]
        parts = piece_str.split()
        color = parts[0]
        piece_type = parts[1]
        position = eval(row["Position"])
        context.game_service.setup_piece(
            context.board, piece_type, color, position
        )


@when("{color} moves the {piece_type} from {from_pos} to {to_pos}")
def step_move_piece(context, color, piece_type, from_pos, to_pos):
    context.move_result = context.game_service.execute_move(
        context.board, eval(from_pos), eval(to_pos)
    )


@then("the move is legal")
def step_assert_move_legal(context):
    assert (
        context.move_result.is_legal
    ), f"Expected move to be legal, but it was illegal: {context.move_result.error_message}"


@then("the move is illegal")
def step_assert_move_illegal(context):
    assert (
        not context.move_result.is_legal
    ), "Expected move to be illegal, but it was legal"


@then("{color} wins immediately")
def step_assert_win(context, color):
    assert (
        context.move_result.is_game_over
    ), "Expected game to be over, but it continues"
    assert context.move_result.winner.value == color, (
        f"Expected {color} to win, "
        f"but winner is {context.move_result.winner}"
    )


@then("the game is not over just from that capture")
def step_assert_game_continues(context):
    assert (
        not context.move_result.is_game_over
    ), "Expected game to continue, but it's over"
