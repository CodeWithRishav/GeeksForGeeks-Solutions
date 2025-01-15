# User function Template for python3

from collections import defaultdict


class Solution:

    # Function to find the length of the longest subarray with sum 'k'
    def longestSubarray(self, arr, k):
        # Creating a default dictionary
        # Default value for non-existent keys will be 0
        um = defaultdict(lambda: 0)

        # Initializing variables
        current_sum = 0
        maxLen = 0

        # Iterating through the array
        for i in range(len(arr)):  # Use len(arr) instead of n
            # Calculating the current sum
            current_sum += arr[i]

            # Checking if the current sum is equal to 'k'
            if current_sum == k:
                maxLen = i + 1

            # Adding the current sum to the dictionary if it doesn't exist
            if current_sum not in um:
                um[current_sum] = i

            # Checking if the difference between the current sum and 'k' exists in the dictionary
            if (current_sum - k) in um:
                # Updating maxLen if needed
                maxLen = max(maxLen, i - um[current_sum - k])

        # Returning the maximum subarray length
        return maxLen
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends