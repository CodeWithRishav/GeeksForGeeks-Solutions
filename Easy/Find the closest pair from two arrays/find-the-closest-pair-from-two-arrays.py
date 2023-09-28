class Solution:
    def printClosest(self, arr, brr, n, m, x):
        # Swap n and m
        n, m = m, n

        # Initialize the diff between pair sum and x
        diff = float("inf")

        # res_l and res_r are result indexes from arr and brr respectively
        res_l, res_r = 0, 0

        # Start from the left side of arr and the right side of brr
        l, r = 0, n - 1

        while l < m and r >= 0:
            # If this pair is closer to x than the previously found closest, update res_l, res_r, and diff
            if abs(arr[l] + brr[r] - x) < diff:
                res_l, res_r = l, r
                diff = abs(arr[l] + brr[r] - x)

            # If the sum of this pair is more than x, move to the smaller side
            if arr[l] + brr[r] > x:
                r -= 1
            else:
                # Move to the greater side
                l += 1

        # Create a list to store the result
        result = [arr[res_l], brr[res_r]]
        return result





#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends