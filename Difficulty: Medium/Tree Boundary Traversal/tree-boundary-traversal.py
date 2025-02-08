#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:

    def printLeaves(self, root, res):
        if root is None:
            return

        self.printLeaves(root.left, res)

        # Add to result if it's a leaf node
        if not root.left and not root.right:
            res.append(root.data)

        self.printLeaves(root.right, res)

    # A function to print all left boundary nodes, except a leaf node
    # Print the nodes in TOP DOWN manner
    def printBoundaryLeft(self, root, res):
        if root is None:
            return

        if root.left:
            # to ensure top-down order, add the node before
            # recursive call for the left subtree
            res.append(root.data)
            self.printBoundaryLeft(root.left, res)
        elif root.right:
            res.append(root.data)
            self.printBoundaryLeft(root.right, res)

        # do nothing if it is a leaf node

    # A function to print all right boundary nodes, except a leaf node
    # Print the nodes in BOTTOM UP manner
    def printBoundaryRight(self, root, res):
        if root is None:
            return

        if root.right:
            # to ensure bottom-up order, call first for right subtree
            self.printBoundaryRight(root.right, res)
            res.append(root.data)
        elif root.left:
            self.printBoundaryRight(root.left, res)
            res.append(root.data)

        # do nothing if it is a leaf node

    # A function to do boundary traversal of a given binary tree
    def boundaryTraversal(self, root):
        res = []
        if root is None:
            return res

        # Add root to result
        res.append(root.data)

        # Print the left boundary in top-down manner
        self.printBoundaryLeft(root.left, res)

        # Print all leaf nodes
        self.printLeaves(root.left, res)
        self.printLeaves(root.right, res)

        # Print the right boundary in bottom-up manner
        self.printBoundaryRight(root.right, res)

        return res




#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        res = obj.boundaryTraversal(root)
        for i in res:
            print(i, end=" ")
        print('')
        print("~")

# } Driver Code Ends