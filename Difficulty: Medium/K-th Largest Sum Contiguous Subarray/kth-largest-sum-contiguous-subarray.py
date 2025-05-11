from typing import List
import heapq


class Solution:

    def kthLargest(self, arr, k) -> int:
        N = len(arr)
        pre = [0] * (N + 1)
        pre[0] = 0
        pre[1] = arr[0]

        # Calculating prefix sum of the array.
        for i in range(2, N + 1):
            pre[i] = pre[i - 1] + arr[i - 1]

        # Creating a min-heap to store the k largest elements.
        pq = []

        # Iterating over all subarrays to find the k largest elements.
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                x = pre[j] - pre[i - 1]

                # If heap size is less than k, add current element to heap.
                if len(pq) < k:
                    heapq.heappush(pq, x)
                # If current element is larger than smallest element in heap,
                # replace smallest element with current element.
                elif pq[0] < x:
                    heapq.heappop(pq)
                    heapq.heappush(pq, x)

        # Returning the kth largest element.
        return pq[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends