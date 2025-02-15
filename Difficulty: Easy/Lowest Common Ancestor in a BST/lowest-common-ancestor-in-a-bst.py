'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Function to find LCA of n1 and n2, assuming
    # that both nodes n1 and n2 are present in BST
    def LCA(self, root, n1, n2):

        while root:

            # If both n1 and n2 are smaller than root,
            # then LCA lies in left
            if root.data > n1.data and root.data > n2.data:
                root = root.left

            # If both n1 and n2 are greater than root,
            # then LCA lies in right
            elif root.data < n1.data and root.data < n2.data:
                root = root.right

            # Else Ancestor is found
            else:
                break

        return root
        
    



#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    q = deque()

    # Push the root to the queue
    q.append(root)

    # Starting from the second element
    i = 1
    while len(q) > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)

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
            q.append(currNode.right)
        i += 1
    return root


if __name__ == "__main__":
    t = int(input())
    ob = Solution()
    for _ in range(t):
        s = input()
        root = buildTree(s)

        # Read n1 and n2 from two separate lines
        x = int(input())
        y = int(input())
        n1 = Node(x)
        n2 = Node(y)
        print(ob.LCA(root, n1, n2).data)
        print("~")

# } Driver Code Ends