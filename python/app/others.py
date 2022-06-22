from collections import deque
import math
import time

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

def factorization(n: int) -> list:
    """nを素因数分解する関数

    Args:
        n (int): 素因数分解する数

    Returns:
        list: [素因数のリスト, 指数のリスト]
    """
    fact = []
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            fact.append([i, cnt])

    if n != 1:
        fact.append([n, 1])

    return fact

def shakutori():
    #尺取り法の例
    #https://atcoder.jp/contests/abc229/tasks/abc229_d
    S = input()
    K = int(input())
    # S[l_index:r_index]が選んでる状態 半開区間に注意
    l_index = 0
    r_index = 0
    dot_counter = 0
    ans = 0
    # l_indexが右端にいくまで
    while l_index < len(S):
        # r_indexが終端の右側にあるとき
        if r_index == len(S):
            if S[l_index] == ".":
                dot_counter -= 1
                l_index += 1
        # r_indexを含んでみる
        elif S[r_index] == ".":
            # 条件がOKならr_indexを進める
            if dot_counter + 1 <= K:
                r_index += 1
                dot_counter += 1
            else:
            # 条件がダメなのでl_indexを進めたい
                if l_index == r_index:
                    # l_index == r_indexなら両方進める
                    l_index += 1
                    r_index += 1
                else:
                    # l_indexを進める
                    if S[l_index] == ".":
                        dot_counter -= 1
                        l_index += 1
        else:
        # 条件がOKならr_indexを進める
            r_index += 1
            
        # scoreの計算
        if (r_index - l_index) > ans:
            ans = r_index - l_index
        
        print(ans)

def fast_pow(x:int, n: int, mod: int) -> int:
    """x^nをmodで割った余りをlog(n)で求める関数

    Args:
        x (int): 底
        n (int): 指数
        mod (int): 法

    Returns:
        int: x^nをmodで割った余り
    """
    
    rui = x%mod
    ans = 1
    while(n):
        if n&1:
            ans = (ans * rui)%mod
        rui = (rui**2)%mod
        n = n >> 1
    return ans

def gcd(a: int, b: int) -> int:
    """a, bの最大公約数を求める関数

    Args:
        a (int): 自然数
        b (int): 自然数

    Returns:
        int: a, bの最大公約数
    """
    if a==0:
        return b
    elif b==0:
        return a
    elif a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)
        
        
    


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
    print("=========", end='\n\n')
    print("fast pow")
    now = time.time()
    ans = fast_pow(x=5, n=1000000, mod=3)
    print(f"fast_pow ans={ans} {time.time()-now}s")
    now = time.time()
    print(f"simple_pow ans={(5**1000000)%3} {time.time()-now}s")
    print("=========", end='\n\n')
    print("gcd")
    print(gcd(a=36, b=24))
    print(gcd(a=17, b=13))
    print(0//2)
    
