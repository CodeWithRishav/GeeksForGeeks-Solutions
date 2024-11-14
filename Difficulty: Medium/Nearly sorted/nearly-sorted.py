#User function Template for python3

import heapq


class Solution:

    def nearlySorted(self, arr, k):
        # Create a min heap for the first k+1 elements
        pq = arr[:k + 1]
        heapq.heapify(pq)  # Turn the list into a min-heap

        id = 0
        # Process the remaining elements
        for i in range(k + 1, len(arr)):
            arr[id] = heapq.heappop(
                pq)  # Extract the minimum element from the heap
            heapq.heappush(pq, arr[i])  # Add the current element to the heap
            id += 1

        # Extract the remaining elements from the heap
        while pq:
            arr[id] = heapq.heappop(pq)
            id += 1


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends