from typing import List


class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for p in price:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, p + buy1)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, p + buy2)

        return sell2
        



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
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends