from Util.Algorithms import Algorithm
from Map.map import Map

def printout(dfs, bfs):
    print("Solution: ")
    print("\tdfs:", dfs)
    print("\tbfs:", bfs)

def main():
    print("== Pacman Solver ==")
    print("Pilih peta: ")
    print(" 1. Peta Simple 3x4")
    print(" 2. Peta Hard 6x6")
    i = input("pilih: ")
    if i is '1':
        print("== Map Simple 3x4 dipilih ==")
        print(" - start = (1, 1)")
        print(" - Dot obj = (2, 3)")
        dfs = Algorithm.dfs(Map.graph1, (1, 1), (2, 3))
        bfs = Algorithm.bfs(Map.graph1, (1, 1), (2, 3))
        printout(dfs, bfs)
    elif i is '2':
        print("== Map Hard 6x6 dipilih ==")
        print(" - start = (1, 1)")
        print(" - Dot obj = (6, 6)")
        dfs = Algorithm.dfs(Map.graph, (1, 1), (6, 6))
        bfs = Algorithm.bfs(Map.graph, (1, 1), (6, 6))
        printout(dfs, bfs)
    else:
        print("Check your input")

if __name__ == '__main__':
    main()