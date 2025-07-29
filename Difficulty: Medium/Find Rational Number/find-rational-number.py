class Solution:

    def compare(self, a, b, p, q):
        lhs = a * q
        rhs = p * b
        if lhs == rhs:
            return 0
        return 1 if lhs > rhs else -1

    def findRI(self, a, b, p, q):
        n = len(a)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            cmp = self.compare(a[mid], b[mid], p, q)
            if cmp == 0:
                return mid
            elif cmp < 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1