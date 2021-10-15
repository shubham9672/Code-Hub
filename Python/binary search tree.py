# Python3 program to implement
# optimized delete in BST.


class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do
# inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):
    # If the tree is empty,
    # return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


# Given a binary search tree
# and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root

    elif key > root.key:
        root.right = deleteNode(root.right, key)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If one of the children is empty

    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    # If both children exist

    succParent = root

    # Find Successor

    succ = root.right

    while succ.left != None:
        succParent = succ
        succ = succ.left

    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    # Copy Successor Data to root

    root.key = succ.key

    return root


# Driver code
""" Let us create following BST
		  50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# print("Inorder traversal of the given tree")
# inorder(root)

# print("\nDelete 20")
# root = deleteNode(root, 50)
# print("Inorder traversal of the modified tree")
# inorder(root)
#


print(root.left.key)
# print("\nDelete 30")
# root = deleteNode(root, 30)
# print("Inorder traversal of the modified tree")
# inorder(root)
#
# print("\nDelete 50")
# root = deleteNode(root, 50)
# print("Inorder traversal of the modified tree")
# inorder(root)
