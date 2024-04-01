
from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        s = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            s.append(node.data)
            inorder(node.right)
        inorder(root)
        
        ans = 0
        def mergesort(arr):
            nonlocal ans
            if len(arr) <= 1:
                return arr
                
            mi = len(arr)//2
            a = mergesort(arr[:mi])
            b = mergesort(arr[mi:])
            i, j, ret = 0, 0, []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ans += len(a)-i
                    ret.append(b[j])
                    j += 1
            if i < len(a):
                ret.extend(a[i:])
            if j < len(b):
                ret.extend(b[j:])
            return ret
        mergesort(s)
        return ans
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        root = inputTree();
        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        
        print(res)
        

# } Driver Code Ends