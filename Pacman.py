from queue import PriorityQueue

graph = {
    (1, 1): {(1, 2), (2, 1)},
    (1, 2): {(2, 2)},
    (2, 2): {(2, 3)},
    (2, 3): {(1, 3), (2, 4), (3, 4)},
    (1, 3): {(2, 3)},
    (2, 4): {(2, 5)},
    (2, 5): {(2, 6), (3, 5)},
    (2, 6): {(1, 6)},
    (1, 6): {(2, 6)},
    (2, 1): {(3, 1)},
    (3, 1): {(4, 1)},
    (4, 1): {(4, 2), (5, 1)},
    (4, 2): {(3, 2)},
    (3, 2): {(3, 3)},
    (3, 3): {(2, 3), (4, 2)},
    (4, 4): {(3, 4)},
    (3, 4): {(3, 5)},
    (3, 5): {(3, 6), (4, 5)},
    (3, 6): {(3, 5)},
    (4, 5): {(5, 5)},
    (4, 3): {(5, 3)},
    (5, 1): {(5, 2), (6, 1)},
    (5, 3): {(6, 3), (5, 4)},
    (5, 2): {(6, 2)},
    (6, 2): {(6, 3)},
    (5, 4): {(6, 4)},
    (6, 4): {(6, 5)},
    (5, 5): {(6, 5)},
    (6, 5): {(6, 6)}
}

graph1 = {
        (1, 1): {(1, 2), (2, 1)},
        (1, 2): {(2, 2), (1, 3)},
        (1, 3): {(1, 4), (1, 2)},
        (1, 4): {(1, 3), (2, 4)},
        (2, 1): {(1, 1), (1, 3)},
        (2, 2): {(2, 3), (1, 2)},
        (2, 3): {(2, 2)},
        (2, 4): {(1, 4), (3, 4)},
        (3, 1): {(2, 1), (3, 2)},
        (3, 2): {(3, 1), (3, 3)},
        (3, 3): {(3, 2), (3, 4)},
        (3, 4): {(2, 4), (3, 3)},
}

def dfs(graph, start, goal):
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))

    while not fringe.empty():
        depth, current_node, path, visited = fringe.get()

        if current_node == goal:
            return path + [current_node]

        visited = visited + [current_node]

        child_nodes = graph[current_node]
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path + [node], visited))

    return path


if __name__ == "__main__":

    path = dfs(graph, (1, 1), (6, 6))
    path1 = dfs(graph1, (3, 3), (2, 3))

    print("path:", path)
    print("path:", path1)