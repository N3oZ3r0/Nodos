def DFS(G, s):
    vis, pila = {s}, [s]
    print(vis)
    print(pila)
    print(G[pila[-1]])

    print("\n<< PROFUNDIDAD >> nodo de salida -->", s , end=" ")
    while pila:
        flag = 0
        for i in G[pila[-1]]:
            if i not in vis:
                pila.append(i)
                vis.add(i)
                flag = 1
                print(i, end = " ")
                break
        if not flag:
            pila.pop()