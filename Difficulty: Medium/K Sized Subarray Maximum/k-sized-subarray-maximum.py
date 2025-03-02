class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):

        res = []
        d = deque()
        n = len(arr)

        #iterating over first k elements or first window of array.
        for i in range(k):

            #for every element, the previously smaller elements
            #are useless so removing them from deque.
            while len(d) and arr[i] >= arr[d[-1]]:
                d.pop()

            #adding new element at back of deque.
            d.append(i)

        #iterating over the rest of the elements.
        for i in range(k, n):

            #the element at the front of the deque is the largest
            #element of previous window, so adding it to the list.
            res.append(arr[d[0]])

            #removing the elements which are out of this window.
            while len(d) and d[0] <= i - k:
                d.popleft()

            #removing all elements smaller than the element being
            #added currently (removing useless elements).
            while len(d) and arr[i] >= arr[d[-1]]:
                d.pop()

            #adding new element at back of deque.
            d.append(i)

        #the element at the front of the deque is the largest
        #element of last window, so adding it to the list.
        res.append(arr[d[0]])
        d.popleft()

        #returning the list.
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

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
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends