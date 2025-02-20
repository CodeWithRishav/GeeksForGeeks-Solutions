
import heapq


class Solution:
    # Function to find the median of a stream of data
    def getMedian(self, arr):

        # Max heap to store the smaller half of numbers
        leftMaxHeap = []

        # Min heap to store the greater half of numbers
        rightMinHeap = []

        res = []

        for num in arr:
            # Insert new element into max heap (negating for max behavior)
            heapq.heappush(leftMaxHeap, -num)

            # Move the top of max heap to min heap to maintain order
            temp = -heapq.heappop(leftMaxHeap)
            heapq.heappush(rightMinHeap, temp)

            # Balance heaps if min heap has more elements
            if len(rightMinHeap) > len(leftMaxHeap):
                temp = heapq.heappop(rightMinHeap)
                heapq.heappush(leftMaxHeap, -temp)

            # Compute median based on heap sizes
            if len(leftMaxHeap) != len(rightMinHeap):
                median = -leftMaxHeap[0]
            else:
                median = (-leftMaxHeap[0] + rightMinHeap[0]) / 2.0

            res.append(median)

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends