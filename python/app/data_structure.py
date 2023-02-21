
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
        self.n_unique_root = n_node

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
        self.n_unique_root -= 1
        if self.rank_list[node1] < self.rank_list[node2]:
            self.root_list[node1] = node2
        else:
            self.root_list[node2] = node1
            if self.rank_list[node1] == self.rank_list[node2]:
                self.rank_list[node1] += 1
        return None

"""
https://qiita.com/takayg1/items/c811bd07c21923d7ec69 から引用
"""
class SegmentTree:

    def __init__(self, init_val: list, segfunc: "関数", ide_ele: int):
        """セグ木の初期化
        Args:
            init_val (list): クエリを投げたい配列
            segfunc (関数): 評価関数
            ide_ele (int): 評価関数の単位元
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k: int, x: int):
        """k番目の値をxに変える log(N)
        Args:
            k (int): 変えたい値のindex
            x (int): 変える値
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l: int, r: int) -> int:
        """_summary_
        Args:
            l (int): 閉区間の左側 0-index
            r (int): 開区間の右側 0-index
        Returns:
            int:区間[l, r)の評価関数による値
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
"""
https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e から引用
"""
#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = 2**31 - 1
#################

class LazySegmentTree_RUQ:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(l, r, x): 区間[l, r)をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        num: n以上の最小の2のべき乗
        data: 値配列(1-index)
        lazy: 遅延配列(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
            """
            伝搬する対象の区間を求める
            lm: 伝搬する必要のある最大の左閉区間
            rm: 伝搬する必要のある最大の右開区間
            """
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間 
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        """
        区間[l, r)の値をxに更新
        l, r: index(0-index)
        x: update value
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res
"""
https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e から引用
"""
#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = 2**31 - 1
#################

class LazySegmentTree_RSQ:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    add(l, r, x): 区間[l, r)にxを加算 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        num: n以上の最小の2のべき乗
        data: 値配列(1-index)
        lazy: 遅延配列(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
            """
            伝搬する対象の区間を求める
            lm: 伝搬する必要のある最大の左閉区間
            rm: 伝搬する必要のある最大の右開区間
            """
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間 
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if not v:
                continue
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.data[2 * i] += v
            self.data[2 * i + 1] += v
            self.lazy[i] = 0

    def add(self, l, r, x):
        """
        区間[l, r)の値にxを加算
        l, r: index(0-index)
        x: additional value
        """
        *ids, = self.gindex(l, r)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.data[l] += x
                l += 1
            if r & 1:
                self.lazy[r - 1] += x
                self.data[r - 1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1]) + self.lazy[i]


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res




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
    print("=========", end='\n\n')

    # UnionFindTree
    print("UnionFindTree")
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
    print(uf.n_unique_root)
    print("=========", end='\n\n')
    print("segment tree")

    """
    単位元
    min: min(x, y) float("inf")
    max: max(x, y) -float("inf")
    区間和: x+y 0
    区間積: x*y 1
    最大公約数 math.gcd(x, y) 0
    """
    arr = [2, 4, 2, 6, 7]
    st = SegmentTree(init_val=arr, segfunc=lambda x, y: max(x, y), ide_ele=-float("inf"))
    print("arr", arr)
    print("tree", st.tree)
    print(st.query(1, 4))
    print(st.query(1, 5))
    st.update(4, -1)
    print(st.query(1, 5))
    