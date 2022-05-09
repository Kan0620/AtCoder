import bisect

def n_range_LR(sorted_list: list, L: int, R: int) -> int:
    """sort済みの整数のみが入ってるリストの中でL以上R以下の数字の個数を返す関数
    計算量はO(log(len(sorted_list)))

    Args:
        sorted_list (list): sort済みのリスト
        L (int): 探す数字の最小値
        R (int):探す数字の最大値

    Returns:
        int: sort済みのリストの中でL以上R以下の数字の個数
    """
    return bisect.bisect_left(sorted_list, R+1) - bisect.bisect_right(sorted_list, L-1)

def binary_search_with_is_equal(sorted_list: list, query_num: float):
    """sort済みの整数のみが入ってるリストの中でL以上R以下の数字の個数を返す関数
    計算量はO(log(len(sorted_list)))

    Args:
        sorted_list (list): sort済みのリスト
        query_num (int): 探す数字
        
    Returns:
        int: 同じものがあるかのbool
        list: ない場合は1つのindex, ある時は左右でのindex
    """
    l_index = bisect.bisect_left(sorted_list, query_num)
    r_index = bisect.bisect_right(sorted_list, query_num)
    if l_index == r_index:
        return False, [l_index]
    else:
        return True, [l_index, r_index]



if __name__ == "__main__":
    a = [0, 0, 1, 1, 1, 2, 3, 3]
    print(n_range_LR(a, 1, 2))
    print(n_range_LR(a, -1, 0))
    print(binary_search_with_is_equal(a, 1))
    print(binary_search_with_is_equal(a, 2))
    print(binary_search_with_is_equal(a, 2.5))
    
    
    