class Solution:
    def minRow(self,n,m,a):
        #code here
        min1 = float('inf')
        ans = 1
        for i in range(len(a)):
            x = a[i].count(1)
            if x<min1:
                min1 = x
                ans = i+1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends