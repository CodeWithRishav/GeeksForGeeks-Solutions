from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        kmap = {}
        for ele in arr:
            if ele not in kmap:
                kmap[ele] = 1
            else:
                kmap[ele] += 1
        for ele in arr:
            req1 = ele + x
            req2 = ele - x
            if x == 0:
                if kmap[ele] > 1:
                    return 1
                # return-1
            else:
                if req1 in kmap or req2 in kmap:
                    return 1
        return -1



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

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.findPair(n, x, arr)

        print(res)

# } Driver Code Ends