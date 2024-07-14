#User function Template for python3

from collections import Counter
class Solution:
    def segregate0and1(self, arr):
        ctn = 0
        for i in arr:
            if i  == 0:
                ctn += 1
        
        for i in range(ctn):
            arr[i] = 0
        for j in range(ctn,len(arr)):
            arr[j] = 1


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

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.segregate0and1(arr)

        print(*arr)

# } Driver Code Ends