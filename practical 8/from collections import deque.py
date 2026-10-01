from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Build Binary Tree
def build_tree():
    data = int(input("Enter the Data: "))

    if data == -1:
        return None

    root = Node(data)

    print("For left node")
    root.left = build_tree()

    print("For right node")
    root.right = build_tree()

    return root
    
def bfs_traversal(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        temp = queue.popleft()

        print(temp.data, end=" ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)
            
def dfs_traversal(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        temp = stack.pop()

        print(temp.data, end=" ")
        
        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)
root = build_tree()

print("\nBFS Traversal:")
bfs_traversal(root)

print("\nDFS Traversal:")
dfs_traversal(root)
