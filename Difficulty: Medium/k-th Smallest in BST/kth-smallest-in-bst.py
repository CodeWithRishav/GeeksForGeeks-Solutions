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
    

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:

    def kthSmallest(self, root, k):
        ksmall = -1  # store the Kth smallest
        curr = root  # to store the current node

        while curr != None:

            # Like Morris traversal if current does
            # not have left child rather than
            # printing as we did in inorder, we
            # will just increment the count as the
            # number will be in an increasing order
            if curr.left == None:
                if k == 1:
                    ksmall = curr.data
                k -= 1
                curr = curr.right

            else:
                pre = curr.left

                while pre.right != None and pre.right != curr:
                    pre = pre.right

                if pre.right == None:
                    pre.right = curr
                    curr = curr.left

                else:

                    if k == 1:
                        ksmall = curr.data
                    k -= 1
                    pre.right = None
                    curr = curr.right

        return ksmall  # return the found value


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k1=int(input())
        print(Solution().kthSmallest(root, k1))
        
        print("~")
# } Driver Code Ends