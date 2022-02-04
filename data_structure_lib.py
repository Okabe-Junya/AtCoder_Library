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
        return
    
    
    # 表示
    def display(self):
        return

        
                
from random import randint
l = [randint(1, 100) for _ in range(20)]
print(sorted(l))
tree = BST(l)
print("min", tree.search_min())
print("max", tree.search_max())