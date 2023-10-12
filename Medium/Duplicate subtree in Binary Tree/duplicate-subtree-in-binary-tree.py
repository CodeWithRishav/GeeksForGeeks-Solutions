import sys
sys.setrecursionlimit(10**6)


class Solution:
    def __init__(self):
        self.subtrees = set()
        self.MARKER = '$'
    
    def dupSubUtil(self, root):
        s = ""

        # If current node is None, return marker
        if root is None:
            return s + self.MARKER

        # If left subtree has a duplicate subtree
        lStr = self.dupSubUtil(root.left)
        if lStr == s:
            return s

        # Do the same for the right subtree
        rStr = self.dupSubUtil(root.right)
        if rStr == s:
            return s

        # Serialize the current subtree
        s = s + str(root.data) + lStr + rStr

        # If the current subtree already exists in the set
        # Note that the size of a serialized tree with a single node is 3
        if len(s) > 3 and s in self.subtrees:
            return ""

        self.subtrees.add(s)

        return s

    def dupSub(self, root):
        # self.subtrees.clear()  # Uncomment this line if you want to clear the set before each call.
        result = self.dupSubUtil(root)

        if result == "":
            return 1
        else:
            return 0


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
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.dupSub(root))
# } Driver Code Ends