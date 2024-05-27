
from typing import List
from collections import defaultdict


class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        M = {}
        dps = [0] * n
        for i, num in enumerate(a):
            dps[i] = 1 + max(dps[M[num - 1]] if (num - 1) in M else 0, dps[M[num + 1]] if (num + 1) in M else 0)
            M[num] = i
        
        return max(dps)
        



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

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.longestSubseq(n, a)

        print(res)

# } Driver Code Ends