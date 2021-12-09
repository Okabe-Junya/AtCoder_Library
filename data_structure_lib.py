#  二分探索
def bin_search(num_list, ky):
    num_list.sort()
    pl = 0
    pr = len(num_list) - 1
    while True :
        pc = (pl + pr) // 2
        if num_list[pc] == ky :
            return pc
        elif num_list[pc] > ky :
            pr = pc - 1
        else :
            pl = pc + 1
        if pl > pr :
            break
    return -1