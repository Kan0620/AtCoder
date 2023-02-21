from email.policy import default
import heapq
from collections import deque, defaultdict
import time

def bellman_ford(n_node: int, edges: list, start_node: int, is_directed=False) -> list:
    """bellman_ford法であるノードからの他のノードへの最短距離を求める方法
    計算量はO(|V||E|)
    
    Args:
        n_node (int): ノードの数
        edges (list): 要素が[ノードの番号, ノードの番号, 距離]となっているリスト
        start_node (int): 開始ノードのindex
        is_directed(bool): 有効グラフならTrue デフォルトでFalse

    Returns:
        list: ノードのindexに対応した最短距離が要素のlist
    """
    d = [float("inf") for i in range(n_node)]
    for i in range(n_node):
        # これはいらないっぽい？ infに戻す意味がわからない
        # https://qiita.com/takayg1/items/92fb138683ac72b47d86
        #d[i] = float("inf")
        d[start_node] = 0
        while True:
            update = False
            for from_node, to_node, c in edges:
                if (d[from_node] != float("inf")) and (d[to_node] > d[from_node] + c):
                    d[to_node] = d[from_node] + c
                    update = True
                    
            if not is_directed:
                for to_node, from_node, c in edges:
                    if (d[from_node] != float("inf")) and (d[to_node] > d[from_node] + c):
                        d[to_node] = d[from_node] + c
                        update = True
            if not update:
                break
    return d

def dijkstra(n_node: int, edges_dict: dict, start_node: int) -> list:
    """ dijkstra法であるノードからの他のノードへの最短距離を求める方法
    計算量はO(|E|log(|V|))
    
    Args:
        n_node (int): ノードの数
        edges_dict (dict): keyがnodeでvalueは要素が[node, cost]になってるリスト
        start_node (int): 開始ノードのindex
        
    Returns:
        list: ノードのindexに対応した最短距離が要素のlist
    """
    hq = [(0, start_node)]
    from_nodes = [-1]*n_node
    heapq.heapify(hq)
    min_cost = [float("inf")]*n_node
    min_cost[start_node] = 0
    while len(hq) > 0:
        c, from_node = heapq.heappop(hq)
        if c > min_cost[from_node]:
            # 取り出したcostがmin_costを上回っている
            continue
        
        for to_node, cost in edges_dict[from_node]:
            tmp = cost + min_cost[from_node]
            if tmp < min_cost[to_node]:
                min_cost[to_node] = tmp
                heapq.heappush(hq, (tmp, to_node))
                from_nodes[to_node] = from_nodes
                
    return min_cost, from_nodes

def strongly_connected_components(
    n_node: int,
    edges_dict: dict,
    inv_edges_dict: dict
    ) -> list:
    """強連結成分分解 O(|E|+|V|)

    Args:
        n_node (int): エッジの数
        edges_dict (dict): 有向グラフを表す隣接リスト keyがindex, valueがlist
        inv_edges_dict (dict): 逆辺を張った隣接リスト

    Returns:
        list: 強連結成分の二重リスト
    """
    connected_components = []
    is_searched = [False]*n_node
    for start_node in range(n_node):
        
        if not is_searched[start_node]:
            is_can_go = [False]*n_node
            is_can_go[start_node] = True
            is_searched[start_node] = True
            dfs_que = deque([start_node])
            result_que = deque([start_node])
            while len(dfs_que) > 0:
                node = dfs_que.pop()
                for next_node in edges_dict[node]:
                    if not is_searched[next_node]:
                        is_searched[next_node] = True
                        is_can_go[next_node] = True
                        dfs_que.append(next_node)
                        result_que.append(next_node)
            is_gone = [False]*n_node
            for node in result_que:
                if not is_gone[node]:
                    is_gone[node] = True
                    dfs_que = deque([node])
                    components = deque([node])
                    while len(dfs_que) > 0:
                        node = dfs_que.pop()
                        for next_node in inv_edges_dict[node]:
                            if (not is_gone[next_node]) and is_can_go[next_node]:
                                is_gone[next_node] = True
                                dfs_que.append(next_node)
                                components.append(next_node)
                    connected_components.append(list(components))
    return connected_components






if __name__ == "__main__":
    n_node = 7
    edges = [
        [0, 1, 2],
        [0, 2, 5],
        [1, 2, 4],
        [1, 3, 6],
        [2, 3, 2],
        [1, 4, 10],
        [3, 5, 1],
        [4, 5, 3],
        [4, 6, 5],
        [5, 6, 9]
    ]
    now = time.time()
    d = bellman_ford(n_node, edges, 0)
    print(f"bellman_ford: {time.time()-now}", d)
    
    edges_dict = {}
    for from_node, to_node, cost in edges:
        if from_node in edges_dict:
            edges_dict[from_node].append([to_node, cost])
        else:
            edges_dict[from_node] = [[to_node, cost]]
        
        from_node, to_node = to_node, from_node
        
        if from_node in edges_dict:
            edges_dict[from_node].append([to_node, cost])
        else:
            edges_dict[from_node] = [[to_node, cost]]
    now = time.time()        
    d = dijkstra(n_node, edges_dict, 0)
    print(f"dijkstra: {time.time()-now}", d)
    
    E = [
        [0, 1],
        [1, 2],
        [2, 0],
        [2, 3],
        [3, 4],
        [4, 3],
        [4, 5],
        [4, 6],
        [7, 8],
        [8, 7]
    ]
    edges_dict = defaultdict(lambda: [])
    inv_edges_dict = defaultdict(lambda: [])
    for s, e in E:
        edges_dict[s].append(e)
        inv_edges_dict[e].append(s)
    results = strongly_connected_components(
        n_node=9,
        edges_dict=edges_dict,
        inv_edges_dict=inv_edges_dict)
    print(results)
    
    
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import connected_components
    # 入力は1-indexed
    E = list(map(lambda x: [x[0]+1, x[1]+1], E))
    edge = np.array(E, dtype = np.int64).T
    tmp = np.ones(9, dtype = np.int64).T
    graph = csr_matrix((tmp, (edge[:] -1)), (9, len(E)))
    n, results = connected_components(graph, directed = True, connection = 'strong')
    print(results)
    
    