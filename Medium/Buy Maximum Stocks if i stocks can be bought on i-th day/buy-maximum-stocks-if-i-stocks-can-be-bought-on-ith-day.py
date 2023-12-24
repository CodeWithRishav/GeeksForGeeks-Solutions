from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        stocks =[]
        for i in range(n):
            maxs= i+1
            stocks.append((price[i],maxs))
        
        stocks.sort()
        res=0
        
        for i in stocks:
            maxs=i[1]
            price= i[0]
            cnt=0
            while(cnt<maxs and k>=price):
                cnt+=1
                k-=price
                res+=1
        
        return res
        



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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends