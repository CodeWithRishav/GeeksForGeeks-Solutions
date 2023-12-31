from typing import List


class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
        dp = [{} for _ in range(N)]
        return self.solve(0, N, 0, coins, dp)

    def solve(self, i, n, sum, coins, dp):
        if sum == 2024 or (sum and (sum % 20 == 0 or sum % 24 == 0)):
            return True

        if i == n or sum > 2024:
            return False

        if sum in dp[i]:
            return dp[i][sum]

        nt = self.solve(i + 1, n, sum, coins, dp)
        if nt:
            dp[i][sum] = nt
            return nt

        dp[i][sum] = self.solve(i + 1, n, sum + coins[i], coins, dp)
        return dp[i][sum]
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.isPossible(N, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends