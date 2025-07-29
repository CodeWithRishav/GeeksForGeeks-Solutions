class Solution:

    def missingRange(self, arr, low, high):
        s = set(arr)
        ans = []
        for x in range(low, high + 1):
            if x not in s:
                ans.append(x)
        return ans