# Chinese Chess - Object-Oriented Design

## Class Design Overview

### 1. Entity Layer (chess/entities/)

#### Position
```python
class Position:
    def __init__(self, row: int, col: int)

    # Validation
    def is_valid(self) -> bool
    def is_in_palace(self, color: Color) -> bool
    def is_in_red_territory(self) -> bool
    def is_in_black_territory(self) -> bool

    # Calculation
    def distance_to(self, other: Position) -> tuple[int, int]
    def is_orthogonal_to(self, other: Position) -> bool
    def is_diagonal_to(self, other: Position) -> bool
```

#### Board
```python
class Board:
    def __init__(self)

    # Piece Management
    def place_piece(self, piece: Piece, position: Position)
    def remove_piece(self, position: Position) -> Optional[Piece]
    def get_piece(self, position: Position) -> Optional[Piece]
    def is_empty(self, position: Position) -> bool

    # Path Checking
    def is_path_clear(self, from_pos: Position, to_pos: Position) -> bool
    def count_pieces_between(self, from_pos: Position, to_pos: Position) -> int
    def get_pieces_between(self, from_pos: Position, to_pos: Position) -> List[Piece]

    # Game State
    def find_general(self, color: Color) -> Optional[Position]
    def are_generals_facing(self) -> bool
```

#### Piece (Abstract Base Class)
```python
class Piece(ABC):
    def __init__(self, color: Color, piece_type: PieceType)

    @abstractmethod
    def can_move_to(self, target: Position, board: Board) -> bool

    def get_color(self) -> Color
    def get_type(self) -> PieceType
```

#### Move
```python
class Move:
    def __init__(self, piece: Piece, from_pos: Position, to_pos: Position)

    def is_legal(self, board: Board) -> bool
    def execute(self, board: Board) -> MoveResult
    def is_capture(self, board: Board) -> bool
```

#### MoveResult
```python
class MoveResult:
    def __init__(
        self,
        is_legal: bool,
        is_game_over: bool = False,
        winner: Optional[Color] = None,
        error_message: Optional[str] = None
    )
```

### 2. Pieces Layer (chess/pieces/)

Each piece implements specific movement rules:

#### General
```python
class General(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Must stay in palace
        # 2. Move one step orthogonally
        # 3. Cannot face opponent's General
```

#### Guard
```python
class Guard(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Must stay in palace
        # 2. Move one step diagonally
```

#### Rook
```python
class Rook(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Move orthogonally any distance
        # 2. Path must be clear
```

#### Horse
```python
class Horse(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Move in "L" shape (2+1)
        # 2. Check for blocking piece at intermediate position
```

#### Cannon
```python
class Cannon(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Move like Rook when not capturing
        # 2. Must jump exactly one piece to capture
```

#### Elephant
```python
class Elephant(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Move 2 steps diagonally
        # 2. Cannot cross river
        # 3. Midpoint must be empty
```

#### Soldier
```python
class Soldier(Piece):
    def can_move_to(self, target: Position, board: Board) -> bool
        # 1. Move forward before crossing river
        # 2. Can move forward or sideways after crossing
        # 3. Cannot move backward
```

### 3. Game Layer (chess/game/)

#### GameService
```python
class GameService:
    def __init__(self)

    # Board Setup
    def create_empty_board(self) -> Board
    def setup_piece(self, board: Board, piece_type: str, color: str, position: tuple)

    # Move Execution
    def execute_move(
        self,
        board: Board,
        from_pos: tuple,
        to_pos: tuple
    ) -> MoveResult

    # Game State
    def is_game_over(self, board: Board) -> bool
    def get_winner(self, board: Board) -> Optional[Color]
```

## Design Patterns

### 1. Strategy Pattern
Each piece type implements its own movement strategy through `can_move_to()` method.

### 2. Factory Pattern (Optional)
Could use factory to create pieces based on string identifiers.

### 3. Command Pattern
`Move` class encapsulates all information about a move operation.

## Key Design Principles

1. **Single Responsibility**: Each piece class only handles its own movement rules
2. **Open/Closed**: Easy to add new piece types without modifying existing code
3. **Liskov Substitution**: All piece subclasses can be used interchangeably through Piece interface
4. **Dependency Inversion**: High-level game logic depends on Piece abstraction, not concrete pieces

## Validation Layers

1. **Position Validation**: Check if position is within board bounds
2. **Piece Movement Validation**: Check if move follows piece-specific rules
3. **Board State Validation**: Check for path blocking, captures, etc.
4. **Game Rule Validation**: Check for General facing, win conditions, etc.
