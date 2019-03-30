from queue import PriorityQueue
from map.map import Map

def dfs(graph, start, goal):
    visited = []
    path = [start]
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

def bfs(graph, start, goal):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.append(node)

if __name__ == "__main__":
    map1 = Map.graph
    map2 = Map.graph1

    path = dfs(map1, (1, 1), (6, 6))
    path2 = dfs(map1, (1, 1), (2, 3))
    path1 = bfs(map2, (1, 1), (2, 3))

    print("path dfs:", path2)
    print("path bfs:", path1)