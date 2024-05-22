#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3

class Solution:

    # Function to find the smallest maximum distance
    def findSmallestMaxDist(self, stations, K):
        left, right = 1e-6, stations[-1] - stations[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0

            # Counting the number of stations that can be added with the current maximum distance
            for a, b in zip(stations, stations[1:]):
                count += math.ceil((b - a) / mid) - 1

            # Updating the left or right values based on the count
            if count > K:
                left = mid
            else:
                right = mid
        return right
        # Code here

#{ 
 # Driver Code Starts.
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends