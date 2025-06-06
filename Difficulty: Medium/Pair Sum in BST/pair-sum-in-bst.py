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

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    # Function to perform Inorder traversal and store the
    # elements in an array
    def inorderTraversal(self, root, inorder):
        if root is None:
            return

        self.inorderTraversal(root.left, inorder)

        # Store the current node's value
        inorder.append(root.data)

        self.inorderTraversal(root.right, inorder)

    # Function to find if there exists a pair with a
    # given sum in the BST
    def findTarget(self, root, target):
        # Create an auxiliary array and store Inorder traversal
        inorder = []
        self.inorderTraversal(root, inorder)

        # Use two-pointer technique to find the pair with given sum
        left, right = 0, len(inorder) - 1

        while left < right:
            currentSum = inorder[left] + inorder[right]

            # If the pair is found, return true
            if currentSum == target:
                return True

            # If the current sum is less than the target,
            # move the left pointer
            if currentSum < target:
                left += 1

            # If the current sum is greater than
            # the target, move the right pointer
            else:
                right -= 1

        return False


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        summ = int(input())
        root=buildTree(s)
        ans = Solution().findTarget(root,summ)
        if (ans==False):
            print(0)
        else:
            print(1)
        print("~")
# } Driver Code Ends