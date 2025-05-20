class Solution:

    def maxDepth(self, n):
        # finding the most distant leaf node from given node
        if n is None:
            return 0
        return 1 + max((self.maxDepth(n.left), self.maxDepth(n.right)))

    def traverse(self, n, target):
        if n is None:
            # base case
            return (0, 0)

        if n.data == target:
            # target found, hence returning distance from it
            ans = self.maxDepth(n.right)
            ans = max(ans, self.maxDepth(n.left))
            return (ans, 1)

        # this func return 2 integers
        # ans represents a possible answer
        # dist represents distance from target node if it was found in subtree

        ans, dist = self.traverse(n.left, target)
        if dist:
            # dist != 0 means target was found at distance = dist
            ans = max(ans, dist + self.maxDepth(n.right))
            # finding max Depth on right as target was on left
            return (ans, dist + 1)

        ans, dist = self.traverse(n.right, target)
        if dist:
            ans = max(ans, dist + self.maxDepth(n.left))
            # finding max Depth on left as target was on right
            return (ans, dist + 1)

        return (0, 0)

    def minTime(self, root, target):
        return (self.traverse(root, target))[0]