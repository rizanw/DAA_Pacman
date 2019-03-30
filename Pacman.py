from Util.Algorithms import Algorithm
from Map.map import Map

if __name__ == "__main__":
    map1 = Map.graph
    map2 = Map.graph1
    dfs = Algorithm.dfs()
    bfs = Algorithm.bfs()

    path = dfs(map1, (1, 1), (6, 6))
    path2 = dfs(map1, (1, 1), (2, 3))
    path1 = bfs(map2, (1, 1), (2, 3))

    print("path dfs:", path2)
    print("path bfs:", path1)