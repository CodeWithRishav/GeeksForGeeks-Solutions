class Height: 
    def __init__(self): 
        self.height = 0

#Function to check for balanced tree.
def isBalancedUtil(root, height): 
      
    lh = Height() 
    rh = Height() 
  
    #if root is null, we return true.
    if root is None: 
        return True
  
    #calling the function isBalancedUtil recursively for the heights of left 
    #and right subtrees and storing the returned values in l and r.
    l = isBalancedUtil(root.left, lh) 
    r = isBalancedUtil(root.right, rh) 
  
    #height of current node is (max of heights of left and right subtrees) +1.
    height.height = max(lh.height, rh.height) + 1
  
    #if difference between heights of left and right subtrees is 2 or more 
    #than 2 then this node is not balanced so we return false.
    if abs(lh.height - rh.height) >= 2: 
        return False  
  
    #if this node is balanced and left and right subtrees are balanced 
    #then we return true.
    else:
        return l and r

class Solution: 
    #Function to check whether a binary tree is balanced or not.   
    def isBalanced(self,root):
        height = Height() 
        return isBalancedUtil(root,height)




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
        if ob.isBalanced(root):
            print(1) 
        else:
            print(0)
# } Driver Code Ends