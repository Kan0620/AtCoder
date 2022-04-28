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
    d = bellman_ford(n_node, edges, 0)
    print(d)