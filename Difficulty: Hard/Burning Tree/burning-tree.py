#User function Template for python3

class Solution:
    def maxDepth(self, n):
        # finding the most distant leaf node from given node
        if n is None:
            return 0
        return 1 + max(( self.maxDepth(n.left) , self.maxDepth(n.right) ))
    
    def traverse(self,n,target):
        if n is None:
            # base case
            return (0,0)
        
        if n.data==target:
            # target found, hence returning distance from it
            ans = self.maxDepth(n.right)
            ans = max( ans, self.maxDepth(n.left) )
            return (ans,1)
        
        # this func return 2 integers
        # ans represents a possible answer
        # dist represents distance from target node if it was found in subtree
        
        ans, dist = self.traverse(n.left, target)
        if dist:
            # dist != 0 means target was found at distance = dist
            ans = max( ans, dist+self.maxDepth(n.right) )
            # finding max Depth on right as target was on left
            return (ans,dist+1)
        
        ans, dist = self.traverse(n.right, target)
        if dist:
            ans = max( ans, dist+self.maxDepth(n.left) )
            # finding max Depth on left as target was on right
            return (ans,dist+1)
        
        return (0,0)
    
    def minTime(self,root,target):
        return ( self.traverse(root,target) )[0]



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
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends