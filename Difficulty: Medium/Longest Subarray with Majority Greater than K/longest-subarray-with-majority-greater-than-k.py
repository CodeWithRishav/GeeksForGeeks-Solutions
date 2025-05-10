#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

    def longestSubarray(self, arr, k):
        n = len(arr)

        # To store the first occurrence of each prefix sum
        prefixMap = {}
        res = 0
        prefixSum = 0

        for i in range(n):
            if arr[i] > k:
                prefixSum += 1
            else:
                prefixSum -= 1

            # If the prefix sum is positive, subarray from the start to i is valid
            if prefixSum > 0:
                res = i + 1

            # If this prefix sum has been seen before, check for a valid subarray
            if prefixSum - 1 in prefixMap:
                res = max(res, i - prefixMap[prefixSum - 1])

            # Store the first occurrence of the prefix sum
            if prefixSum not in prefixMap:
                prefixMap[prefixSum] = i

        return res


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends