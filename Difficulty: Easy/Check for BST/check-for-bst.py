#User function Template for python3


class Solution:

    INT_MAX = 4294967296
    INT_MIN = -4294967296

    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, node):
        return (self.isBSTUtil(node, self.INT_MIN, self.INT_MAX))

    def isBSTUtil(self, node, mini, maxi):

        #an empty tree is BST so we return true.
        if node is None:
            return True

        #returning false if this node violates the min/max constraint.
        if node.data < mini or node.data > maxi:
            return False

        #otherwise checking the subtrees recursively.
        #tightening the min or max constraint.
        return (self.isBSTUtil(node.left, mini, node.data - 1)
                and self.isBSTUtil(node.right, node.data + 1, maxi))




#{ 
 # Driver Code Starts
#Initial Template for Python 3
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
        if Solution().isBST(root):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends