from collections import deque


def BFS(G, s):
    vis, Q = {s}, deque([s])
    print("\n<<   ANCHURA   >> nodo de salida -->", s , end=" ")
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                vis.add(v)
                Q.append(v)
                print(v, end = " ")