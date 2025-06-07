import random

def generate_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]
    
    def carve(x, y):
        dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size-1 and 1 <= ny < size-1 and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                maze[x + dx//2][y + dy//2] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(1, 1)
    maze[size-2][size-2] = 0
    return maze

def solve_maze(maze, x=1, y=1, path=[]):
    if (x, y) == (len(maze)-2, len(maze)-2):
        path.append((x, y))
        return True
    if maze[x][y] == 1:
        return False
    maze[x][y] = 1
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if solve_maze(maze, x+dx, y+dy, path):
            path.append((x, y))
            return True
    return False

def display_maze(maze, path=[]):
    maze_copy = [row[:] for row in maze]
    for x, y in path:
        maze_copy[x][y] = '*'
    for row in maze_copy:
        print(''.join(' ' if cell == 0 else ('*' if cell == '*' else '█') for cell in row))

# User input
size = int(input("Enter odd maze size (e.g., 11): "))
if size % 2 == 0:
    print("Size must be odd.")
else:
    maze = generate_maze(size)
    path = []
    solve_maze([row[:] for row in maze], path=path)
    display_maze(maze, path[::-1])
