# Maze Escape Game
# Player moves with W/A/S/D and tries to reach E.
# The program can also find the shortest path using BFS.

# maze stored as a 2D list (# = wall, . = path, P = start, E = exit)
maze = [
    ['P', '.', '.', '#', '#'],
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', 'E']
]

rows = 5
cols = 5


def print_maze(player_row, player_col):
    # print the maze and show the player's position
    print()
    for i in range(rows):
        line = ""
        for j in range(cols):
            if i == player_row and j == player_col:
                line = line + "P "
            elif maze[i][j] == 'P':
                line = line + ". "   # old start position is just a path now
            else:
                line = line + maze[i][j] + " "
        print(line)
    print()


def play_game():
    # player starts at row 0, col 0
    player_row = 0
    player_col = 0
    moves = 0

    print("\nUse W (up), A (left), S (down), D (right). Press Q to quit.")
    print_maze(player_row, player_col)

    while True:
        key = input("Enter move: ").upper()

        if key == 'Q':
            print("You quit the game.")
            break

        # find the new position according to the key
        new_row = player_row
        new_col = player_col

        if key == 'W':
            new_row = player_row - 1
        elif key == 'A':
            new_col = player_col - 1
        elif key == 'S':
            new_row = player_row + 1
        elif key == 'D':
            new_col = player_col + 1
        else:
            print("Invalid key '" + key + "'. Use W, A, S or D only.")
            continue

        # check if the move is outside the maze
        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
            print("Cannot move outside the maze. Player stays at (" +
                  str(player_row) + ", " + str(player_col) + ")")
            print("Moves: " + str(moves))
            print_maze(player_row, player_col)
            continue

        # check if there is a wall
        if maze[new_row][new_col] == '#':
            print("Wall ahead. Move blocked. Player stays at (" +
                  str(player_row) + ", " + str(player_col) + ")")
            print("Moves counted: " + str(moves))
            print_maze(player_row, player_col)
            continue

        # valid move
        player_row = new_row
        player_col = new_col
        moves = moves + 1
        print("Player moved to (row " + str(player_row) + ", col " +
              str(player_col) + ") | Moves: " + str(moves))
        print_maze(player_row, player_col)

        # check if player reached the exit
        if maze[player_row][player_col] == 'E':
            print("You escaped the maze! Total moves: " + str(moves))
            break


def shortest_path():
    # BFS (Breadth First Search) to find the shortest path from start to exit
    start = (0, 0)
    queue = [(0, 0, 0)]       # each item is (row, col, steps)
    visited = [start]

    # directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(queue) > 0:
        current = queue.pop(0)   # take the first item
        r = current[0]
        c = current[1]
        steps = current[2]

        # if we reached the exit, we are done
        if maze[r][c] == 'E':
            print("Shortest path length: " + str(steps) + " steps")
            return steps

        for d in directions:
            nr = r + d[0]
            nc = c + d[1]

            # inside the maze, not a wall, and not visited before
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.append((nr, nc))
                    queue.append((nr, nc, steps + 1))

    print("No path found from start to exit.")
    return -1


def main():
    while True:
        print("\n===== MAZE ESCAPE GAME =====")
        print("1. Play game")
        print("2. Shortest path")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            shortest_path()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Wrong choice. Please enter 1, 2 or 3.")


main()