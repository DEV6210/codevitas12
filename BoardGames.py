from collections import deque

def rotate_clockwise_90(x, y):
    return (y, -x)

def rotate_anticlockwise_90(x, y):
    return (-y, x)

def rotate_180(x, y):
    return (-x, -y)

def is_valid(nx, ny, M, N, grid):
    return 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0

def bfs(grid, source, destination, move_rule, M, N):
    queue = deque([(source[0], source[1], 0)])  
    visited = set()
    visited.add((source[0], source[1]))

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == destination:
            return steps

        for dx, dy in [
            move_rule,                        
            rotate_clockwise_90(*move_rule),  
            rotate_anticlockwise_90(*move_rule),  
            rotate_180(*move_rule)            
        ]:
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny, M, N, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1

# Input
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
source = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))
move_rule = tuple(map(int, input().split()))

result = bfs(grid, source, destination, move_rule, M, N)
print(result,end="")