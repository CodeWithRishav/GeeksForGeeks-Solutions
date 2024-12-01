#User function Template for python3

class Solution:

    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):

        #using hash table to store count of each character.
        occurences = [0 for i in range(256)]

        #iterating over the string.
        for char in s:
            occurences[ord(char)] += 1

        for i in range(len(s)):
            #if count of current character is 1, we return it.
            if (occurences[ord(s[i])] == 1):
                return s[i]

        #if there is no non-repeating character then we return '$'.
        return '$'
    
    


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


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

        print("~")

# } Driver Code Ends