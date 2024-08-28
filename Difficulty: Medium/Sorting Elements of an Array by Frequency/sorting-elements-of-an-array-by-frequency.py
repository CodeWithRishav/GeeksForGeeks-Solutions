#User function Template for python3
 
class Solution:
    # Function to sort the array according to frequency of elements.
    def sortByFreq(self, arr):
        # Create a frequency dictionary to store the frequency of each element
        freq_dict = {}
        for num in arr:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # Sort the array first by frequency (in decreasing order) and then by the element's value (in increasing order)
        sorted_arr = sorted(arr, key=lambda x: (-freq_dict[x], x))

        return sorted_arr



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
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends