#User function Template for python3

import heapq

class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr):
        # If there is only one rope, no cost is required to connect.
        if len(arr) <= 1:
            return 0
        
        # Create a min-heap from the array
        heapq.heapify(arr)
        
        total_cost = 0
        
        # While more than one rope is left
        while len(arr) > 1:
            # Extract the two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # The cost of connecting them
            cost = first + second
            total_cost += cost
            
            # Push the resulting rope back into the heap
            heapq.heappush(arr, cost)
        
        return total_cost


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

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
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends