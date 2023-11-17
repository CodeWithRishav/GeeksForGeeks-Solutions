#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
        


# } Driver Code Ends
#User function Template for python3



'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        if root is None:
            return None
            
        # Helper function to convert BTree to DLL
        def convert(node):
            
            if node is None:
                return

            # Declare prev and head as nonlocal
            nonlocal prev, head

            # Convert left subtree
            convert(node.left)

            # Create a node
            dll_node = Node(node.data)

            # If it is the first node, make it head
            if prev is None:
                head = dll_node
            else:  # If there is a previous node
                prev.right = dll_node
                dll_node.left = prev

            # Update prev pointer
            prev = dll_node

            # Convert right subtree
            convert(node.right)

        # Initialize prev and head
        prev = None
        head = None

        # Perform conversion operation
        convert(root)
        
        # Find the last node to connect it first node and make it a CDLL
        last = Node(None)
        last = head
        while last.right:
            last = last.right

        # Connect the last node to the head
        last.right = head
        head.left = last

        return head


#{ 
 # Driver Code Starts.
def displayList(head):
    itr=head
    while(itr.right!=head):
        print(itr.data,end=" ")
        itr=itr.right
    print(itr.data,end=" ")
    print()
    head = itr
    while(itr.left!=head):
        print(itr.data,end=" ")
        itr=itr.left
    print(itr.data, end=" ")
    
 
    
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
        head=Solution().bTreeToClist(root)
        displayList(head)
        print()
        
        

        




# } Driver Code Ends