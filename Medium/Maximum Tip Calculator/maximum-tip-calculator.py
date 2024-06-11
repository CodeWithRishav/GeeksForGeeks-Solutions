
from typing import List


class Solution:
    def key(self,item):
        return abs(item[0]-item[1])

    def maxTip(self,n,x,y,arr,brr):
        combo=[]
        for i in range(n):
            combo.append([arr[i],brr[i]])
        combo.sort(key=self.key,reverse=True)
        ans=0
        for i in range(n):
            if (combo[i][0]>=combo[i][1] and x) or (not y):
                ans+=combo[i][0]
                x-=1
            else:
                ans+=combo[i][1]
                y-=1
        return ans
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends