from collections import deque


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


# 木構造のノード
class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


# 二分探索木
class BST:
    def __init__(self, num_list) -> None:
        self.root = None
        for num in num_list:
            self.insert_node(num)
        return
    
    
    # 最小値の探索
    def search_min(self):
        root = self.root
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root.data
        

    # 最大値の探索
    def search_max(self):
        root = self.root
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root.data
    
    
    # 探索
    def search_tree(self, key) -> bool:
        root = self.root
        if root is None:
            return False
        while True:
            if root.data == key:
                return True
            elif root.data > key:
                if root.left:
                    root = root.left
                else:
                    return False
            else:
                if root.right:
                    root = root.right
                else:
                    return False
    
    
    # 挿入
    def insert_node(self, data):
        root = self.root
        if root is None:
            self.root = Node(data)
            return
        while True:
            if root.data > data:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(data)
                    return
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(data)
                    return
    
    
    # 削除
    def delete_node(self, data):
        if not self.search_tree(data):
            print("{} is not in the tree".format(data))
            return
        return
    
    
    # 表示
    def display(self):
        return
    
    # 深さ優先探索（木）
    # 行き掛け
    
    # 通りがけ
    
    # 帰りがけ
    
    # 幅優先探索（木）


# 深さ優先探索（グラフ）
def dfs(e, v, seen): # e: エッジの集合，v: ノード，seen: 既に訪れたノードの集合
    seen[v] = True
    m = len(e[0])
    for n in range(m):
        if e[v][n] & (seen[n] == False) & (n != v):
            dfs(e, n, seen)
    return seen

"""
n, m = map(int, input().split())
e = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    e[a][b] = 1
    
ans = 0
for i in range(1, n + 1):
    seen = [False for _ in range(n + 1)]
    if seen[i] == False:
        l = dfs(e, i, seen)
        ans += sum(l)
print(ans)
"""


# 幅優先探索

# ダイクストラ法

# ワーシャルフロイド法

# 最大流

# 最小カット

# 二部マッチング

# union-find
