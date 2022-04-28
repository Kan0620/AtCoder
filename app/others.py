from collections import deque

def euler_tour(edges, root_node):
    
    edges_dict = {}
    for from_node, to_node in edges:
        if from_node in edges_dict:
            edges_dict[from_node].add(to_node)
        else:
            edges_dict[from_node] = {to_node}
        from_node, to_node = to_node, from_node
        if from_node in edges_dict:
            edges_dict[from_node].add(to_node)
        else:
            edges_dict[from_node] = {to_node}
    
    in_t = {}
    out_t = {}
    tour_q = deque()

    def DFS(node, t):
        t += 1
        tour_q.append(node)
        in_t[node] = t
        for n in edges_dict[node]:
            if not n in in_t:
                t = DFS(n, t)
                tour_q.append(node)
        t += 1
        out_t[node] = t
        return t
    
    DFS(root_node, -1)
    
    return in_t, out_t, tour_q

if __name__ == "__main__":
    edges = [
        [1, 4],
        [2, 1],
        [2, 5],
        [3, 2]
    ]
    root_node = 1
    in_t, out_t, tour_q = euler_tour(edges, root_node)
    print(in_t)
    print(out_t)
    print(tour_q)
