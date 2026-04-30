import sys

sys.setrecursionlimit(10000)

def loadBoard(filename):
    """
    Reads a board from a .txt file.
    Each line of the file becomes one row; each character becomes one cell.
    Returns a 2-D list of characters, e.g. [['W','.','B'], ...]
    """
    board = []
    with open(filename, 'r') as f:
        for line in f:
            row = list(line.rstrip('\n'))   # keep spaces / dots / W / B
            if row:                          # skip completely empty lines
                board.append(row)
    return board

def switchPlayer(current_player):
    """Returns the opposite player ('W' ↔ 'B')."""
    return 'B' if current_player == 'W' else 'W'

def floodfill(matrix, x, y, color):
    """
    Recursively fills every '.' cell reachable from (x, y) with 'color'.
    x = row index, y = column index.

    Bug fixes from original template:
      • Added bounds checks at the TOP of the function (cleaner & safe).
      • Original had len(matrix[x]) where len(matrix) was needed (rows vs cols swapped).
    """
    # Bounds check + only fill empty cells
    if x < 0 or x >= len(matrix):
        return
    if y < 0 or y >= len(matrix[x]):
        return
    if matrix[x][y] != '.':
        return

    matrix[x][y] = color                        # paint this cell

    floodfill(matrix, x - 1, y, color)          # up
    floodfill(matrix, x + 1, y, color)          # down
    floodfill(matrix, x, y - 1, color)          # left
    floodfill(matrix, x, y + 1, color)          # right

def _collect_region(board, x, y, region):
    """
    Recursively marks every '.' cell reachable from (x,y) with '#' (a temp
    marker) and records its coordinates in 'region'.
    Called by find_inside to map out each enclosed pocket before coloring it.
    """
    rows = len(board)
    cols = len(board[0])

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if board[x][y] != '.':
        return

    board[x][y] = '#'          # mark as visited
    region.append((x, y))

    _collect_region(board, x - 1, y, region)
    _collect_region(board, x + 1, y, region)
    _collect_region(board, x, y - 1, region)
    _collect_region(board, x, y + 1, region)

def find_inside(board):
    """
    Identifies every empty territory, decides which player owns it, and
    fills it with a lowercase marker:
        'w' → owned by White
        'b' → owned by Black
        '?' → contested (borders both colors; not scored)

    Algorithm
    ---------
    1. Flood-fill every '.' cell touching the board edge with 'O'
       (these cells are "outside" — not enclosed by anyone).
    2. Scan for remaining '.' cells.  For each connected pocket:
         a. Collect all cells in the pocket (_collect_region → '#').
         b. Inspect every neighbor of the pocket to see which stone
            colors border it.
         c. Assign fill color based on border colors.
    3. Restore 'O' cells to '.' (neutral open space).

    Modifies board IN PLACE and also returns it.
    """
    rows = len(board)
    cols = len(board[0])

    # ── Step 1: mark "outside" open space ───────────────────────────────────
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '.' and (r == 0 or r == rows - 1 or
                                        c == 0 or c == cols - 1):
                floodfill(board, r, c, 'O')

    # ── Step 2: handle each enclosed pocket ─────────────────────────────────
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '.':
                # Collect this connected pocket
                region = []
                _collect_region(board, r, c, region)

                # Which stone colors border this pocket?
                border_colors = set()
                for (rx, ry) in region:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = rx + dx, ry + dy
                        if 0 <= nx < rows and 0 <= ny < cols:
                            if board[nx][ny] in ('W', 'B'):
                                border_colors.add(board[nx][ny])

                # Decide ownership
                if border_colors == {'W'}:
                    fill = 'w'
                elif border_colors == {'B'}:
                    fill = 'b'
                else:
                    fill = '?'   # contested or unreachable — not scored

                # Paint the pocket
                for (rx, ry) in region:
                    board[rx][ry] = fill

    # ── Step 3: restore neutral open space ──────────────────────────────────
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = '.'

    return board

def countScore(board):
    """
    Counts scored territories after find_inside has been called.
    'w' cells → White points
    'b' cells → Black points
    Returns [white_score, black_score].
    """
    white = sum(row.count('w') for row in board)
    black = sum(row.count('b') for row in board)
    return [white, black]

def printBoard(board):
    """
    Prints the board with column and row indices for readability.

    Example (small board):
          0 1 2 3 4
        0 . W . . .
        1 W . W . .
        2 . W . . .
    """
    cols = len(board[0])
    rows = len(board)

    # Column header (wraps at 10 to keep single-digit spacing)
    col_header = "   " + " ".join(str(c % 10) for c in range(cols))
    print(col_header)

    # Top border
    print("  +" + "-" * (cols * 2 - 1) + "+")

    for r, row in enumerate(board):
        row_str = " ".join(cell for cell in row)
        print(f"{r:2}|{row_str}|")

    # Bottom border
    print("  +" + "-" * (cols * 2 - 1) + "+")
    print()

def main():
    filename = input("Enter the board filename (e.g. board1.txt): ").strip()

    # 1. Load
    board = loadBoard(filename)

    # 2. Show original board
    print("\n── Original Board ──────────────────────────────")
    printBoard(board)

    # 3. Score (fills territories in place)
    find_inside(board)

    # 4. Show scored board
    print("── Scored Board (w = White territory, b = Black territory) ──")
    printBoard(board)

    # 5. Tally and announce winner
    scores = countScore(board)
    white_score, black_score = scores

    print(f"  White Score: {white_score}")
    print(f"  Black Score: {black_score}")
    print()

    if white_score > black_score:
        print(f"★ White wins with a score of {white_score} vs {black_score}! ★")
    elif black_score > white_score:
        print(f"★ Black wins with a score of {black_score} vs {white_score}! ★")
    else:
        print(f"★ It's a tie! Both players scored {white_score}. ★")

if __name__ == "__main__":
    main()