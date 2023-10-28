# Solution with recursion O(2^r+c)

'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
'''


def get_path(maze):
    if not maze:
        return None
    path = []
    if is_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return None


def is_path(maze, row, col, path):
    # if out of bounds or not available, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    is_at_origin = (row == 0) and (col == 0)

    # if there's a path from the start to here, add my location
    if (
        is_at_origin
        or is_path(maze, row, col - 1, path)
        or is_path(maze, row - 1, col, path)
    ):
        point = (row, col)
        path.append(point)
        return True

    return False


# Solution with memoization
def get_path_memoized(maze):
    if not maze:
        return None
    path = []
    failed_points = set()
    if is_path_memoized(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


def is_path_memoized(maze, row, col, path, failed_points):
    # If out of bounds or not availabe, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    point = (row, col)

    # if we've already visisted this cell, return
    if point in failed_points:
        return False

    is_at_origin = (row == 0) and (col == 0)

    # If there's a path from start to my current location, add my location
    if (
        is_at_origin
        or is_path_memoized(maze, row, col - 1, path, failed_points)
        or is_path_memoized(maze, row - 1, col, path, failed_points)
    ):
        path.append(point)
        return True

    failed_points.add(point)
    return False


if __name__ == "__main__":
    print(get_path([[True, True], [True, True]]))
    print(get_path_memoized([[True, True], [False, True]]))
