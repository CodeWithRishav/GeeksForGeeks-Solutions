class Solution:
    ans=0   
    mp=dict()
    
    #Recursive function to calculate the sum of all paths in the binary tree
    def sumK_util(self, root, s, cur, mod):
        global ans
        global mp
        
        #If the current node is null, return
        if(root==None):
            return
        
        #Updating the answer by adding the count of paths with sum (cur+root.data-s)
        ans=ans+mp[cur+root.data-s]
        
        #If the answer exceeds the modulus value, take the modulo
        if(ans>=mod):
            ans%=mod
        
        #If the current sum is equal to the target sum, increment the answer
        if(cur+root.data==s):
            ans=ans+1
        
        #Incrementing the count of current sum in the map
        mp[cur+root.data]+=1
        
        #Recursively calling the function for left and right child with updated current sum
        self.sumK_util(root.left,s,cur+root.data,mod)
        self.sumK_util(root.right,s,cur+root.data,mod)
        
        #Decrementing the count of current sum in the map
        mp[cur+root.data]-=1
        
        #If the count becomes negative, add the modulus value to it
        if(mp[cur+root.data]<0):
            mp[cur+root.data]+=mod
    
    #Function to find the sum of all paths with target sum
    def sumK(self, root, k):
        global ans
        global mp
        
        #Initializing the answer and the map
        ans=0
        mp=defaultdict(lambda:0)
        
        #Defining the modulus value
        mod=pow(10,9)+7
        
        #Calling the recursive function to calculate the sum of all paths
        self.sumK_util(root,k,0,mod)
        
        #Returning the final answer
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)
from collections import deque
from collections import defaultdict
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
        d=int(input())
        ob = Solution()
        print(ob.sumK(root,d))
        
# } Driver Code Ends