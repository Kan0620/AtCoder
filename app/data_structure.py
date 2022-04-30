import heapq
"""
NOTE: 優先度付きキューは元々あるのでmain部分に使用例
"""






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
    