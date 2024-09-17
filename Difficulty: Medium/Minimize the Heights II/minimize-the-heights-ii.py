#User function Template for python3

class Solution:
    # Function to find the minimum difference between the maximum and minimum element after modifying the elements
    def getMinDiff(self, arr, k):
        n = len(arr)
        # Sorting the array in ascending order
        arr.sort()
        # Initializing the answer with the difference between the last and first element
        ans = arr[n - 1] - arr[0]

        # Initializing temporary variables for minimum and maximum elements
        tempmin = arr[0]
        tempmax = arr[n - 1]

        # Iterating through the elements of the array
        for i in range(1, n):
            # If the current element is less than k or the last element is less than k, move to the next iteration
            if arr[i] < k or arr[n - 1] < k:
                continue
            # Calculating the minimum and maximum possible values for the elements
            tempmin = min(arr[0] + k, arr[i] - k)
            tempmax = max(arr[i - 1] + k, arr[n - 1] - k)

            # Updating the answer with the minimum difference between the updated maximum and minimum elements
            ans = min(ans, tempmax - tempmin)

        # Returning the final minimum difference
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends