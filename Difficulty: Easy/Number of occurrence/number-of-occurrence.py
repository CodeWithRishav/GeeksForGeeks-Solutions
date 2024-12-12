class Solution:

    def countFreq(self, arr, target):
        # Get the index of the first occurrence of x
        low = bisect.bisect_left(arr, target)

        # If element is not present, return 0
        if low == len(arr) or arr[low] != target:
            return 0

        # Get the index of the last occurrence of x
        high = bisect.bisect_right(arr, target)

        # Return the count of occurrences
        return high - low


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends