class Solution:

    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        res = arr[n - 1] - arr[0]

        # For all indices i, increment
        # arr[0...i-1] by k and decrement arr[i...n-1] by k
        for i in range(1, len(arr)):
            # Impossible to decrement height  of ith tower by k, continue
            if arr[i] - k < 0:
                continue
            minH = min(arr[0] + k, arr[i] - k)
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)
            res = min(res, maxH - minH)

        return res