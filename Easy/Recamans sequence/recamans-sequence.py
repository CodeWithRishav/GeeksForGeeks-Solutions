#User function Template for python3

from typing import List
from collections import deque

class Solution:
    def recamanSequence(self,n):
        ans = [0]
        num_set = {0}

        for i in range(1, n):
            num = ans[i - 1]
            if num - i < 0 or (num - i) in num_set:
                ans.append(num + i)
                num_set.add(num + i)
            else:
                ans.append(num - i)
                num_set.add(num - i)

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends