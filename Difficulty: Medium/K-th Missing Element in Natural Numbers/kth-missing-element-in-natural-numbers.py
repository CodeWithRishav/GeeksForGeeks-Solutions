class Solution:

    def findKthSmall(self, arr, k):
        arr.sort()
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k