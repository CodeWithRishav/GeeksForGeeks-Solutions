class Solution:

    def leafNodes(self, preorder):
        s = []
        leaves = []
        n = len(preorder)

        # Iterate through the preorder list
        for i in range(n - 1):
            found = False

            # Push current node if it's greater
            # than the next node
            if preorder[i] > preorder[i + 1]:
                s.append(preorder[i])
            else:
                # Pop elements from stack until current node is
                # less than or equal to top of stack
                while s and preorder[i + 1] > s[-1]:
                    s.pop()
                    found = True

            # If a leaf node is found, add it to the
            # leaves list
            if found:
                leaves.append(preorder[i])

        # Since the rightmost element is always
        # a leaf node
        leaves.append(preorder[-1])

        return leaves