def bit_serch(n: int):
    """2**n上の全探索
    計算量はO(n*2**n)

    Args:
        n
    """
    for i in range(1<<n):
        exist_index_list = []
        for j in range(n):
            if (i>>j)&1:
                exist_index_list.append(j)
        print(exist_index_list)

def traveling_salesman_problem(n_node: int, edges: list) -> int:
    """bitDPで巡回セールスマン問題を解く スタートするのはindexが0のノードから

    Args:
        n_node (int): ノードの数
        edges (list): edges (list): 要素が[ノードの番号, ノードの番号, 距離]となっているリスト
        
    Returns:
        int: _description_
    """
    #全集合の数
    V = 1 << n_node
    dp = [[float('inf')]*n_node]*V
    dp
    
    
    
    
    
    
if __name__ == "__main__":
    bit_serch(3)