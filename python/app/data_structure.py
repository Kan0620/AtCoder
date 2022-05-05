import heapq

"""
NOTE: 優先度付きキューは元々あるのでmain部分に使用例
"""
class UnionFindTree:
    def __init__(self, n_node: int):
        """初期化

        Args:
            n_node (int): 要素の数
        """
        self.n_node = n_node
        self.root_list = [i for i in range(n_node)]
        self.rank_list = [0]*n_node
        
    def __find_root(self, node: int) -> int:
        """あるノードのrootのindexを返す

        Args:
            node (int): rootが知りたいノードのindex

        Returns:
            int: rootのindex
        """
        if self.root_list[node] == node:
            return node
        else:
            # 辺の縮約 簡単のためrankは変えない
            self.root_list[node] = self.__find_root(self.root_list[node])
            return self.root_list[node]
        
    def is_same_group(self, node1: int, node2: int) -> bool:
        """あるノードとあるノードが同じグループか調べる

        Args:
            node1 (int): ノードのindex
            node2 (int): ノードのindex

        Returns:
            bool: 同じグループかどうかのbool
        """

        return self.__find_root(node1) == self.__find_root(node2)
    
    def unite(self, node1: int, node2: int):
        """あるノードとあるノードを同じグループにする

        Args:
            node1 (int): ノードのindex
            node2 (int): ノードのindex
        """
        node1 = self.__find_root(node1)
        node2 = self.__find_root(node2)
        if node1 == node2:
            return None
        
        if self.rank_list[node1] < self.rank_list[node2]:
            self.root_list[node1] = node2
        else:
            self.root_list[node2] = node1
            if self.rank_list[node1] == self.rank_list[node2]:
                self.rank_list[node1] += 1
        return None
        





if __name__ == "__main__":
    
    # 優先度付きキュー
    # 数の追加, 最小値の取り出しをlog(N)で行う
    a = [7,5,3,2,4,8,10,1]
    # aがheapqになる
    print("heapq")
    heapq.heapify(a)
    print(a)
    # 値の追加
    heapq.heappush(a,7)
    print(a)
    # (最小)値の取り出し
    print(heapq.heappop(a))
    print(a)
    a = [(8, 2), (2, 4), (3, 0)]
    heapq.heapify(a)
    print(heapq.heappop(a))
    
    # UnionFindTree
    print("\nUnionFindTree")
    uf = UnionFindTree(10)
    edges = [
        [1, 3],
        [3, 5],
        [3, 8],
        [2, 4]
    ]
    for node1, node2 in edges:
        uf.unite(node1, node2)
    print(uf.is_same_group(2, 3))
    print(uf.is_same_group(1, 5))
    print(uf.rank_list)
    print(uf.root_list)