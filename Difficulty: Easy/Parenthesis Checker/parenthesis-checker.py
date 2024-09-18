#User function Template for python3

class Solution:
    def ispar(self, x):
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        for char in x:
            if char in matching_bracket.values():
                stack.append(char)
            elif char in matching_bracket:
                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                stack.pop()
        
        return not stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")

# } Driver Code Ends