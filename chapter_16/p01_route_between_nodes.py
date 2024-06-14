import unittest
from collections import deque
from typing import Dict, Set, Deque, Any

from collections import deque
from typing import Dict, Set, Deque, Any

def is_route(graph: Dict[Any, Set[Any]], start: Any, end: Any, visited: Set[Any] = None) -> bool:
    visited = visited or set()
    
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
            
    return False


def is_route_bfs(graph: Dict[Any, Set[Any]], start: Any, end: Any, visited: Set[Any] = None) -> bool:
    visited = visited or set()
    queue: Deque[Any] = deque([start])

    while queue:
        node = queue.pop()
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                if adjacent == end:
                    return True
                queue.append(adjacent)
                
    return False

def is_route_bidirectional(graph: Dict[Any, Set[Any]], start: Any, end: Any) -> bool:
    if start == end:
        return True

    visited_start, visited_end = {start}, {end}
    queue_start, queue_end = deque([start]), deque([end])

    while queue_start and queue_end:
        node_start = queue_start.popleft() if queue_start else None
        node_end = queue_end.popleft() if queue_end else None

        if node_start in visited_end or node_end in visited_start:
            return True

        if node_start:
            for adjacent in graph[node_start]:
                if adjacent not in visited_start:
                    visited_start.add(adjacent)
                    queue_start.append(adjacent)
        if node_end:
            for adjacent in graph[node_end]:
                if adjacent not in visited_end:
                    visited_end.add(adjacent)
                    queue_end.append(adjacent)

    return False


class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert actual == expected

    def test_is_route_bidirectional(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bidirectional(self.graph, start, end)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
