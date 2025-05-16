import heapq


class Solution:

    def findSmallestRange(self, arr):
        n = len(arr)
        k = len(arr[0])
        heap = []
        maxVal = float('-inf')

        # Push the first element of each
        # list into the min-heap
        for i in range(n):
            heapq.heappush(heap, (arr[i][0], i, 0))
            maxVal = max(maxVal, arr[i][0])

        minRange = float('inf')
        minEl = maxEl = -1

        while True:
            minVal, row, col = heapq.heappop(heap)

            # Update range if better
            if maxVal - minVal < minRange:
                minRange = maxVal - minVal
                minEl = minVal
                maxEl = maxVal

            # If we've reached the end of a list, break
            if col + 1 == k:
                break

            # Push next element from the same list
            nextVal = arr[row][col + 1]
            heapq.heappush(heap, (nextVal, row, col + 1))
            maxVal = max(maxVal, nextVal)

        return [minEl, maxEl]
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends