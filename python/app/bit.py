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

def traveling_salesman_problem(n_node: int, edges: list, start_node: int) -> int:
    
    
    
    
    
if __name__ == "__main__":
    bit_serch(3)