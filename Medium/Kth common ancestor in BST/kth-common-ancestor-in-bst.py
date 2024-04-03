#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.arr = []
        self.visited = False
        
    def LCA(self, root, x, y):
        if not root:
            return None
        if root.data == x or root.data == y:
            return root
        a = self.LCA(root.left, x, y)
        b = self.LCA(root.right, x, y)
        if a and b:
            return root
        if a:
            return a
        return b
    
    def rootToNode(self, root, node):
        if not root:
            return
        if not self.visited:
            self.arr.append(root.data)
        if root == node:
            self.visited = True
        self.rootToNode(root.left, node)
        self.rootToNode(root.right, node)
        if not self.visited:
            self.arr.pop()
    
    def kthCommonAncestor(self, root, k, x, y):
        node = self.LCA(root, x, y)
        self.rootToNode(root, node)
        if len(self.arr) < k:
            return -1
        return self.arr[-k]



#{ 
 # Driver Code Starts

#Initial Template for Python 3


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to Build Tree
def buildTree(str):
    # Corner Case
    if len(str) == 0 or str[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = str.split()

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    queue = deque()
    queue.append(root)

    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.right)

        i += 1

    return root

for _ in range(int(input())):
    s = input()
    root = buildTree(s)
    k, x, y = map(int, input().split())
    if root is None:
        continue
    
    if root.left is None and root.right is None:
        continue
    
    ob = Solution()
    print(ob.kthCommonAncestor(root, k, x, y))


# } Driver Code Ends