class Solution:
    # Function to find the floor of a given value in a binary search tree
    def floor(self, root, x):
        fl = -1  # variable to store the floor
        
        # Loop to traverse the binary search tree
        while(root != None):
            # If the current node's data is equal to x, return the data
            if(root.data == x):
                return root.data
                
            # If the current node's data is less than x, update the floor and move to the right subtree
            if(root.data < x):
                fl = root.data
                root = root.right
            
            # If the current node's data is greater than x, move to the left subtree
            else:
                root = root.left
                
        return fl  # Return the floor value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends