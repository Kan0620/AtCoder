import heapq
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
                
    return min_cost
                
    
    
    


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