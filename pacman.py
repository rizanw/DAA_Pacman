from queue import PriorityQueue
import py

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
    graph = {
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

    print(graph)

    path = dfs(graph, (1, 1), (2, 3))
    print("path", path)
