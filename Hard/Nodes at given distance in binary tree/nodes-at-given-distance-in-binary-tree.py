class Solution:
    def __init__(self):
        self.lst=[]

    # Function to find nodes at k distance below the given root
    def findKDistanceDownNode(self,root,d):
        if d<0 or not root:  # if distance is negative or root is None, return
            return
        if d==0:  # if distance is 0, append root data to the list
            self.lst.append(root.data)
            return
        # recursively find nodes at k distance below left and right child of root
        self.findKDistanceDownNode(root.left,d-1)
        self.findKDistanceDownNode(root.right,d-1)

    # Function to find the target node and its k distance nodes
    def findKDistanceNode(self,root,target,k):
        if not root:  # if tree is empty, return -1
            return -1
        if root.data==target:  # if the current root is the target node
            # find nodes at k distance below the current root
            self.findKDistanceDownNode(root,k)
            return 0

        dl=self.findKDistanceNode(root.left,target,k)  # recursively find target node in left subtree
        
        if dl!=-1:  # if target node found in left subtree
            if dl+1==k:  # if the current root is at k distance from the target
                self.lst.append(root.data)  # append root data to the list
            else:
                # find nodes at k distance below the right child of root
                self.findKDistanceDownNode(root.right,k-dl-2)
            return 1+dl  # return the distance of target node from the current root

        dr=self.findKDistanceNode(root.right,target,k)  # recursively find target node in right subtree

        if dr!=-1:  # if target node found in right subtree
            if dr+1==k:  # if the current root is at k distance from the target
                self.lst.append(root.data)  # append root data to the list
            else:
                # find nodes at k distance below the left child of root
                self.findKDistanceDownNode(root.left,k-dr-2)
            return 1+dr  # return the distance of target node from the current root

        return -1  # return -1 if target node not found

    # Function to find nodes at k distance from the target node
    def KDistanceNodes(self,root,target,k):
        self.lst.clear()  # clear the list to store the result

        self.findKDistanceNode(root,target,k)  # find the target node and its k distance nodes

        self.lst.sort()  # sort the list in ascending order

        return self.lst  # return the list o

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
    # Corner Case
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
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends