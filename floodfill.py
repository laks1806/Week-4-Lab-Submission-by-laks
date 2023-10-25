def flood_fill(input_board, old, new, x, y):
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return input_board  # Stop recursion if coordinates are out of bounds
    if input_board[x][y] == old:
        input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
        # Replace the old value with the new value at (x, y)
        # Using string slicing for the board
        flood_fill(input_board, old, new, x+1, y)  # Recurse down
        flood_fill(input_board, old, new, x-1, y)  # Recurse up
        flood_fill(input_board, old, new, x, y+1)  # Recurse right
        flood_fill(input_board, old, new, x, y-1)  # Recurse left
    return input_board

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(board, ".", "~", 5, 12)

for row in modified_board:
    print(row)

# Different Flood Fill View - Abhi
modified_board = flood_fill(board, ".", "~", 1, 1)

for row in modified_board:
    print(row)
