from collections import deque
import math

def euler_tour(edges: list, root_node: int) -> list:
    """オイラーツアーで根のある木を区間にする

    Args:
        edges (list): 要素が[ノードの番号, ノードの番号, 距離]となっているリスト
        root_node (int): 根のノードのindex

    Returns:
        list: in_t, out_t, tour_q
    """
    
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

def is_prime(n: int) -> bool:
    """nが素数か調べる O(√n)

    Args:
        n (int): 調べたい数字

    Returns:
        bool: 素数かどうかのbool
    """
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n: int) -> list:
    """エラトステネスの篩でnまでの素数を列挙 O(nlog(logn))

    Args:
        n (int): 調べる数

    Returns:
        list: nまでの素数のリスト
    """
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    P = []
    for i, p in enumerate(prime):
        if p:
            P.append(i)
    
    return P

if __name__ == "__main__":
    print("euler_tour")
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
