#User function Template for python3


from collections import defaultdict

class Solution:

    def smallestWindow(self,s, p):
        if not p or not s:
            return "-1"
    
        p_count = defaultdict(int)
        for char in p:
            p_count[char] += 1
    
        required_chars = len(p_count)
        formed_chars = 0
    
        window_counts = defaultdict(int)
        min_window = float("inf"), None, None
    
        left = 0
        for right in range(len(s)):
            character = s[right]
            window_counts[character] += 1
    
            if character in p_count and window_counts[character] == p_count[character]:
                formed_chars += 1
    
            while left <= right and formed_chars == required_chars:
                character = s[left]
    
                if right - left + 1 < min_window[0]:
                    min_window = (right - left + 1, left, right)
    
                window_counts[character] -= 1
                if character in p_count and window_counts[character] < p_count[character]:
                    formed_chars -= 1
    
                left += 1
    
        return "-1" if min_window[0] == float("inf") else s[min_window[1] : min_window[2] + 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends