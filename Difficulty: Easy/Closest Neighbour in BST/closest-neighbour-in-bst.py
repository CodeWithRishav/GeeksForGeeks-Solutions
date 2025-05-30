'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:

    def findMaxFork(self, root, k):

        # Base cases
        if root == None:
            return -1
        if root.data == k:
            return k

        # If root's value is smaller, try in
        # right subtree
        elif root.data < k:
            ans = self.findMaxFork(root.right, k)
            if ans == -1:
                return root.data
            else:
                return ans

        # If root's key is greater, return
        # value from left subtree.
        elif root.data > k:
            return self.findMaxFork(root.left, k)