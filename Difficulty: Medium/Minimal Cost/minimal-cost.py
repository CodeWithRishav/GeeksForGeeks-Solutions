#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

    def minimizeCost(self, k, arr):
        # Initializing a dynamic programming list of size n with -1.
        n = len(arr)
        dp = [-1] * n

        # Setting the first element of the dp list to 0.
        dp[0] = 0

        # Iterate through each element of the dp list.
        for i in range(1, n):
            # Initializing the minimum value to a large number.
            min_v = float('inf')

            # Iterate through each possible k values.
            for j in range(1, k + 1):
                # Checking if the element at i-j is within the bounds of the list.
                if i - j >= 0:
                    # Calculating the current cost.
                    curr = dp[i - j] + abs(arr[i] - arr[i - j])

                    # Updating the minimum value.
                    min_v = min(curr, min_v)

            # Updating the dp list with the minimum value.
            dp[i] = min_v

        # Returning the last element of the dp list as the minimized cost.
        return dp[n - 1]
        # code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends