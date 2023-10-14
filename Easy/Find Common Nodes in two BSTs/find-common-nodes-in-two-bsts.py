class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        
        #creating two stacks for inorder traversals of both BST.
        list1 = []
        list2 = []
        res = []
        while(1):
            
            #pushing the nodes of first BST in list1.
            if(root1):
                list1.append(root1)
                root1 = root1.left
                
            #pushing the nodes of second BST in list2.
            elif(root2):
                list2.append(root2)
                root2 = root2.left
                
            #when both root1 and root2 become NULL
            elif(len(list1)!=0 and len(list2)!=0):
                root1 = list1[len(list1)-1]
                root2 = list2[len(list2)-1]
                
                #if data at current node in two BST's are same, we 
	    		#store it in output list.
                if(root1.data==root2.data):
                    res.append(root1.data)
                    
                    #popping element from both lists.
                    list1.pop()
                    list2.pop()
                    
                    #moving to the inorder successor
                    root1 = root1.right
                    root2 = root2.right
                
                #if data at current node of first BST is smaller than that of 
                #second BST then it's obvious that inorder successors of 
                #current node can have same value as that of second BST node.
                elif(root1.data < root2.data):
                    
                    #popping element from list1.
                    list1.pop()
                    root1 = root1.right
                    #root2 is set to NULL since we need new nodes of first BST.
                    root2 = None
                    
                elif(root1.data > root2.data):
                    
                    #popping element from list2.
                    list2.pop()
                    root2 = root2.right
                    #root1 is set to NULL since we need new nodes of second BST.
                    root1 = None
            else:   
                break
            
        #returning the output list.
        return res

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
        root1=buildTree(s)
        s=input()
        root2=buildTree(s)
        ob = Solution()
        res = ob.findCommon(root1, root2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends