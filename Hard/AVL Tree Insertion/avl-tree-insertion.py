#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    def getHeight(self,rootnode):
        if not rootnode:
            return 0
        return rootnode.height
    def getBalance(self,rootnode):
        if not rootnode:
            return 0
        return self.getHeight(rootnode.left)-self.getHeight(rootnode.right)
    def rotateRight(self,rootnode):
        newroot=rootnode.left
        rootnode.left=rootnode.left.right
        newroot.right=rootnode
        rootnode.height=1+max(self.getHeight(rootnode.left),self.getHeight(rootnode.right))
        newroot.height=1+max(self.getHeight(newroot.left), self.getHeight(newroot.right))
        return newroot
    def rotateLeft(self, rootnode):
        newroot=rootnode.right
        rootnode.right=rootnode.right.left
        newroot.left=rootnode
        rootnode.height=1+max(self.getHeight(rootnode.left),self.getHeight(rootnode.right))
        newroot.height=1+max(self.getHeight(newroot.left), self.getHeight(newroot.right))
        return newroot
    def insertToAVL(self, rootnode, value):
        # add key to AVL (if it is not present already)
        # return root node
        if not rootnode:
            return Node(value)
        elif(value<rootnode.data):
            rootnode.left=self.insertToAVL(rootnode.left,value)
        else:
            rootnode.right=self.insertToAVL(rootnode.right,value)
        rootnode.height=1+max(self.getHeight(rootnode.left),self.getHeight(rootnode.right))
        balance=self.getBalance(rootnode)
        if(balance>1 and value<rootnode.left.data):
            return self.rotateRight(rootnode)
        if(balance>1 and value>rootnode.left.data):
            rootnode.left=self.rotateLeft(rootnode.left)
            return self.rotateRight(rootnode)
        if(balance<-1 and value>rootnode.right.data):
            return self.rotateLeft(rootnode)
        if(balance<-1 and value<rootnode.right.data):
            rootnode.right=self.rotateRight(rootnode.right)
            return self.rotateLeft(rootnode)
        return rootnode




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

# } Driver Code Ends