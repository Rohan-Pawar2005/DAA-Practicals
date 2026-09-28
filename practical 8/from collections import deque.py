from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def level_order_traversal(root):

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


root = build_tree()

print("\nLevel Order Traversal:")
level_order_traversal(root)