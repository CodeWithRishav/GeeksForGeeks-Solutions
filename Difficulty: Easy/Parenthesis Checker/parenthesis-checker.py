
class Solution:

    def isBalanced(self, s):

        # Declare a stack to store the opening brackets
        st = []
        for i in range(len(s)):

            # Check if the character is an opening bracket
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])

            else:
                # If it's a closing bracket, check if the stack is non-empty
                # and if the top of the stack is a matching opening bracket
                if st and ((st[-1] == '(' and s[i] == ')') or
                           (st[-1] == '{' and s[i] == '}') or
                           (st[-1] == '[' and s[i] == ']')):

                    # Pop the matching opening bracket
                    st.pop()
                else:
                    # Unmatched closing bracket
                    return False

        # If stack is empty, return True (balanced), otherwise False
        return not st

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
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends