from typing import List


class Solution:

    def maximumProfit(self, prices):
        ans = 0
        n = len(prices)
        if n == 0:
            return 0

        st = prices[0]
        end = prices[0]

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                end = prices[i]
            else:
                ans += end - st
                st = prices[i]
                end = st

        ans += end - st
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends