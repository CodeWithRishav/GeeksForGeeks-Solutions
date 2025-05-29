'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:

    def sumOfRootToLeaf(self, root, sum, length, maxLen, maxSum):

        # Base case: if the current node is null
        if not root:

            # Checking if the current path has a longer length
            # and update maxLen and maxSum accordingly
            if length > maxLen[0]:
                maxLen[0] = length
                maxSum[0] = sum

            # If the lengths are equal, check if the current sum is
            # greater and update maxSum if necessary
            elif length == maxLen[0] and sum > maxSum[0]:
                maxSum[0] = sum
            return

        # Recursively calculating the sum of
        # the left and right subtrees
        self.sumOfRootToLeaf(root.left, sum + root.data, length + 1, maxLen,
                             maxSum)
        self.sumOfRootToLeaf(root.right, sum + root.data, length + 1, maxLen,
                             maxSum)

    def sumOfLongRootToLeafPath(self, root):
        # Base case: if the tree is empty
        if not root:
            return 0

        # Initializing the variables to store
        # the maximum length and sum
        maxSum = [-float('inf')]
        maxLen = [0]

        # Calling the utility function
        self.sumOfRootToLeaf(root, 0, 0, maxLen, maxSum)

        # Returning the maximum sum
        return maxSum[0]