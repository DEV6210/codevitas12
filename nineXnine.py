def check_sudoku(grid, allowed_numbers, k):
    n = 9  # Size of the grid
    violations = []
    
    # Helper to track the counts of numbers in rows, columns, and blocks
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    blocks = [set() for _ in range(n)]
    
    # Function to find block index
    def get_block_index(row, col):
        return (row // 3) * 3 + (col // 3)
    
    # Analyze the grid
    for r in range(n):
        for c in range(n):
            value = grid[r][c]
            if value != 0:  # Ignoring empty cells
                # Check if the value is in the set for row, column, and block
                block_index = get_block_index(r, c)
                if value in rows[r] or value in cols[c] or value in blocks[block_index]:
                    violations.append((r, c))
                else:
                    rows[r].add(value)
                    cols[c].add(value)
                    blocks[block_index].add(value)

    # Identify the incorrect hinted or filled cells
    incorrect_cells = []
    for r, c in violations:
        if grid[r][c] % 10 != 0:  # Only consider cells filled by Tina
            incorrect_cells.append((r, c))
    
    # Check for hints and see if they can be replaced with allowed numbers
    for r in range(n):
        for c in range(n):
            if grid[r][c] % 10 == 0:  # Hinted cells
                if int(grid[r][c] // 10) not in allowed_numbers:
                    incorrect_cells.append((r, c))
    
    incorrect_count = len(incorrect_cells)

    # Determine the output
    if incorrect_count == 0:
        return "Won"
    elif incorrect_count > k:
        return "Impossible"
    else:
        return [f"{r} {c}" for r, c in incorrect_cells]

# Read input and initialize the grid
grid = []
for _ in range(9):
    line = input().strip().split()
    grid.append([int(num) for num in line])

allowed_numbers = list(map(int, input().strip().split()))
k = int(input().strip())

# Call the function and print results
result = check_sudoku(grid, allowed_numbers, k)
if isinstance(result, str):
    print(result,end="")
else:
    print("\n".join(result),end="")
