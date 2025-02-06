#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:

    def buildIndexMap(self, inorder):
        # Build an index map to store indices of inorder elements
        indexMap = {}
        for index, value in enumerate(inorder):
            indexMap[value] = index
        return indexMap

    def buildUtil(self, inorder, preorder, inStart, preStart, n, indexMap):
        # Base case: if there are no elements to process, return None
        if n <= 0:
            return None

        # Create a new node with the current root from the preorder traversal
        root = Node(preorder[preStart])

        # Find the index of the root in the inorder traversal using the index map
        i = indexMap[preorder[preStart]]

        # Number of elements in the left subtree
        leftSubtreeSize = i - inStart

        # Recursively construct the left and right subtrees
        root.left = self.buildUtil(inorder, preorder, inStart, preStart + 1,
                                   leftSubtreeSize, indexMap)
        root.right = self.buildUtil(inorder, preorder, i + 1,
                                    preStart + leftSubtreeSize + 1,
                                    n - leftSubtreeSize - 1, indexMap)

        return root

    def buildTree(self, inorder, preorder):
        # Create the index map for quick lookup of indices in inorder traversal
        indexMap = self.buildIndexMap(inorder)
        n = len(inorder)  # Total number of nodes
        return self.buildUtil(inorder, preorder, 0, 0, n, indexMap)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends