class Solution:

    # Function to get sum of digits of a number
    def sumOfDigit(self, K):
        sod = 0
        while K > 0:
            sod += K % 10
            K //= 10
        return sod

    def getCount(self, n, d):
        # Binary search to find the least number satisfying the condition
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2

            if mid - self.sumOfDigit(mid) < d:
                low = mid + 1
            else:
                high = mid - 1

        # Subtract from n to get the count
        return n - high