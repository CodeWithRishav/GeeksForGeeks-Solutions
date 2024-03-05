#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        ##Your code here
        stack=[]
        for i , e in enumerate(a):
            if not stack or e<a[stack[-1]]:
                stack.append(i)
        ans=0
        for i in range(n-1,-1,-1):
            while stack and a[stack[-1]]<=a[i]:
                ans=max(ans,i-stack.pop())
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends