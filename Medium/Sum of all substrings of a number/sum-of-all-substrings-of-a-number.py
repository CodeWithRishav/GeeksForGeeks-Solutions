#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings_v1(self,s):
        
        # code here
        N = len(s)
        ss_sum = 0
        for i in range(1, N+1):
            # i is len of substr
            for j in range(0, N-i+1):
                ns = s[j:j+i]
                ss_sum = (ss_sum + int(s[j:j+i])) % (10**9+7)
                
        return ss_sum
            
    def sumSubstrings(self,s):
        n=len(s)
        sm=0
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=(dp[i-1]*10+int(s[i-1])*i)%(10**9+7)
            sm=(sm+dp[i])%(10**9+7)
        return sm


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends