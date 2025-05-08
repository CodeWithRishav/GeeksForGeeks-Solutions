#User function Template for python3

class Solution:

    def findMissing(self, arr):
        n = len(arr)

        diff1 = arr[1] - arr[0]
        diff2 = arr[-1] - arr[-2]
        diff3 = (arr[-1] - arr[0]) // n

        if diff1 == diff2:
            diff = diff1
        elif diff1 == diff3:
            diff = diff1
        else:
            diff = diff2

        if diff == 0:
            return arr[0]

        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # if mid == (nth position of element in AP)-1
            # the missing element will exist in right half
            if (arr[mid] - arr[0]) // diff == mid:
                lo = mid + 1

            # the missing element will exist in left half
            else:
                hi = mid - 1

        # after breaking out of binary search loop the missing element
        # will exist between high and low
        return arr[hi] + diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends