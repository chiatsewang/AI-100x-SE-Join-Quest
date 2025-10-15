# Chinese Chess - Entity Relationship Diagram

## Core Entities

### Board
- **Attributes**:
  - rows: int = 10
  - cols: int = 9
  - pieces: Dict[Position, Piece]

- **Relationships**:
  - Contains multiple Pieces at various Positions

### Position
- **Attributes**:
  - row: int (1-10)
  - col: int (1-9)

- **Methods**:
  - is_valid(): bool
  - is_in_palace(color): bool
  - is_in_red_territory(): bool
  - is_in_black_territory(): bool

### Piece (Abstract)
- **Attributes**:
  - color: Color (Red/Black)
  - position: Position
  - piece_type: PieceType

- **Methods**:
  - can_move_to(target: Position, board: Board): bool (abstract)
  - move_to(target: Position): None

- **Relationships**:
  - Located at one Position
  - Belongs to one Color

### Move
- **Attributes**:
  - piece: Piece
  - from_position: Position
  - to_position: Position
  - is_capture: bool
  - captured_piece: Optional[Piece]

- **Methods**:
  - is_legal(board: Board): bool
  - execute(board: Board): MoveResult

### MoveResult
- **Attributes**:
  - is_legal: bool
  - is_game_over: bool
  - winner: Optional[Color]
  - error_message: Optional[str]

## Piece Hierarchy

```
Piece (Abstract Base)
├── General (將/帥)
├── Guard (士/仕)
├── Rook (車)
├── Horse (馬/傌)
├── Cannon (炮)
├── Elephant (相/象)
└── Soldier (兵/卒)
```

Each concrete piece class implements:
- `can_move_to(target: Position, board: Board): bool`

## Enums

### Color
- RED
- BLACK

### PieceType
- GENERAL
- GUARD
- ROOK
- HORSE
- CANNON
- ELEPHANT
- SOLDIER

## Key Relationships

1. **Board** contains many **Pieces**
2. **Piece** is located at one **Position**
3. **Move** connects a **Piece** from one **Position** to another **Position**
4. **Move** produces a **MoveResult**
5. Each concrete piece (General, Guard, etc.) inherits from **Piece**

## Business Rules

1. Each Position can hold at most one Piece
2. A Piece can only move according to its type's rules
3. Red pieces start from rows 1-5, Black pieces from rows 6-10
4. Capturing opponent's General ends the game immediately
5. Generals cannot face each other directly on the same file
