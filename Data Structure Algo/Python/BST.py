# Inorder traversal of BST always produces sorted output.
# Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]

class Tree:
    def __init__(self, root):
        self.root = Node(root)
    
    def check_bst(self, start):
        if start == None:
            return
        queue = Queue()
        queue.enqueue(start)
        while queue.size()>0:
            node = queue.dequeue()
            if(node.left and node.right):
                if(node.left.value < node.value and node.right.value > node.value):
                    queue.enqueue(node.left)
                    flag=1
                else:
                    flag=0
                    break

            if(node.right and node.left==None):
                if(node.right.value > node.value):
                    queue.enqueue(node.right)
                    flag=1
                else:
                    flag=0
                    break

            if(node.right==None and node.left):
                if(node.left.value < node.value):
                    queue.enqueue(node.left)
                    flag=1
                else:
                    flag=0
                    break

        if(flag==1):
            print("Given Tree is a BST")
        else:
            print("Given Tree is not a BST")
    
    
    # APPROACH FOR SEARCHING BST (BETTER)
    def search(self, root, key): 
    
        if root is None: 
            return
        
        if root.value == key:
            return root.value
    
        # Key is greater than root's key 
        if root.value < key: 
            return self.search(root.right,key) 
        
        # Key is smaller than root's key 
        return self.search(root.left,key) 
        


    # APPROACH FOR SEARCHING BST (WORKS BUT HIGHER TIME COMPLEXITY)
    
    # def search(self, start, key):
    #     if start == None:
    #         return
    #     queue = Queue()
    #     queue.enqueue(start)
    #     while queue.size() > 0:
    #         node = queue.dequeue()
    #         if(key < node.value and node.left != None):
    #             queue.enqueue(node.left)
    #             if(key == node.left.value ):
    #                 return key

    #         if(key > node.value and node.right != None):
    #             queue.enqueue(node.right)
    #             if(key == node.right.value ):
    #                 print("Key Found in BST")
    #                 return key

    def insert(self, start, value):
        if start == None:
            return
        if start.value > value:
            if start.left == None:
                start.left = Node(value)
            else:
                self.insert(start.left, value)
        
        if start.value < value:
            if start.right == None:
                start.right = Node(value)
            else:
                self.insert(start.right, value)
        return value
    
    def delete(self, start, value):
        if start == None:
            return
        print(start.value)
        if start.left.value == value:
            if start.left.left == None and start.left.right == None:   # leaf Node  ie  0 child
                start.left = None
                return

            elif (start.left.left != None and start.left.right == None):   # leaf Node  but  1 child
                start.left = start.left.left
                return
            elif (start.left.left == None and start.left.right != None):   # leaf Node  but  1 child
                start.left = start.left.right
                return

            elif (start.left.left != None and start.left.right != None):   #  Node  but  2 child
                node = start.left
                while(node.right!=None):
                    node = node.right
                start.left = node
                return
           
    
        if start.right.value == value:
            if start.right.left == None and start.right.right == None:   # leaf Node  ie  0 child
                start.right = None
                return
            
            elif (start.right.left != None and start.right.right == None):   # leaf Node  but  1 child
                start.right = start.right.left
                return
            elif (start.right.left == None and start.right.right != None):   # leaf Node  but  1 child
                start.right = start.right.right
                return 
            
            elif (start.right.left != None and start.right.right != None):   #  Node  but  2 child
                node = start.right
                while(node.right!=None):
                    node = node.right
                start.right = node
                return

        if start.value > value:
            self.delete(start.left, value)
        if start.value < value:
            self.delete(start.right, value)


bin_tree = Tree(8)
bin_tree.root.left = Node(3)
bin_tree.root.right = Node(10)
bin_tree.root.left.left = Node(1)
bin_tree.root.left.right = Node(6)
bin_tree.root.left.left.left = Node(0)
bin_tree.root.left.left.right = Node(2)
bin_tree.root.right.left = Node(9)
bin_tree.root.right.right = Node(14)
bin_tree.root.right.right.left = Node(13)
bin_tree.check_bst(bin_tree.root)
print(bin_tree.search(bin_tree.root, 9), "(key) Found in BST")
bin_tree.insert(bin_tree.root, 60)
print(bin_tree.search(bin_tree.root, 60), "(key) Found in BST")
bin_tree.delete(bin_tree.root, 14)
print(bin_tree.search(bin_tree.root, 14), "(key) Found in BST")
bin_tree.check_bst(bin_tree.root)

# print(bin_tree.search(bin_tree.root, 1), "(key) Found in BST")


# OUTPUT OF ABOVE CODE ->
# Given Tree is a BST
# None (key) Found in BST
# 60 (key) Found in BST


# '''
#                 8
#              /     \
#             3       10
#           /   \    /   \
#          1     6  9     14
#        /  \           /   \
#       0    2        13     60            
# '''