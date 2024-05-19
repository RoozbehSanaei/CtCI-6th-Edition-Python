# Solution with recursion O(2^r+c)

'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
'''

'''
unction for Path Finding in a Maze:

    This function checks whether the maze is empty. If it is, the path finding process is not carried out.
    If the maze is not empty, the function attempts to find a path from the bottom-right corner to the top-left corner.
    The function concludes by either returning the found path or indicating that no path exists.

Recursive Function for Determining a Path:

    This recursive function is called to explore the maze for a path from a given position towards the top-left corner.
    The function first ensures that the current position is valid and not blocked. If it's either out of bounds or blocked, the function concludes that the current path is not viable.
    A check is performed to see if the current position is the top-left corner of the maze. If it is, this indicates a successful path has been found.
    If the current position is not the top-left corner, the function proceeds to recursively explore the cell to the left and the cell above the current position.
    When a viable path through either of these adjacent cells is found, the current position is added to the path.
    The function then returns whether a path to the top-left corner can be achieved from the current position.

'''
def get_path(maze):
    if not maze:
        return None
    path = []
    if is_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return None


def is_path(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    is_at_origin = (row == 0) and (col == 0)

    if (
        is_at_origin
        or is_path(maze, row, col - 1, path)
        or is_path(maze, row - 1, col, path)
    ):
        point = (row, col)
        path.append(point)
        return True

    return False


'''
    Function for Path Finding with Memoization:
        This function is responsible for initiating the path-finding process in the maze.
        It starts by checking if the maze is valid and non-empty. If it's not, the function concludes that no path can be found.
        An empty structure is set up to track the path through the maze.
        Another structure is prepared to record points in the maze that have been visited and determined not to lead to a successful path (memoization).
        The function then calls a helper function to determine if a path exists from the bottom-right corner to the top-left corner of the maze.
        Depending on the result from the helper function, it either returns the path found or indicates that no path is available.

    Memoized Recursive Function for Path Checking:
        This helper function checks whether a path exists from a given position in the maze to the top-left corner.
        The function first ensures that the current position is within the bounds of the maze and not blocked. 
            If it's out of bounds or blocked, the function concludes that no path can be found from this position.
        The function also checks if the current position has previously been determined to lead to a dead end. 
            If so, it concludes that no path can be found from this position.
        If the current position is the top-left corner of the maze, it indicates that a successful path has been found.
        If the current position is not the top-left corner, the function recursively checks for a path from the adjacent cell to the left and the cell above the current position.
        If a path is found from either adjacent position, the current position is added to the path.
        If no path is found, the current position is recorded as a dead end to prevent redundant future checks.

'''

def get_path_memoized(maze):
    if not maze:
        return None
    path = []
    failed_points = set()
    if is_path_memoized(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


def is_path_memoized(maze, row, col, path, failed_points):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    point = (row, col)

    if point in failed_points:
        return False

    is_at_origin = (row == 0) and (col == 0)

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
