#User function Template for python3
class Solution:

    def printLargest(self, n, arr):
        A = sorted(arr,key=lambda x:str(x)*10,reverse=True)
        return''.join([str(i)for i in A])



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends