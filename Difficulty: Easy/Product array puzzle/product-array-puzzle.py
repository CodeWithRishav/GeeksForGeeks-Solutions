#User function Template for python3

class Solution:

    def productExceptSelf(self, arr):
        n = len(arr)

        product = 1
        zeroCount = 0

        # Calculate the total product of all elements and count zeros
        for num in arr:
            if num == 0:
                zeroCount += 1
            else:
                product *= num

        # Case 1: If there are more than one zero, return an array of zeros
        if zeroCount > 1:
            return [0] * n  # All zeros

        # Case 2: If there is exactly one zero, set the product at that index
        if zeroCount == 1:
            return [product if num == 0 else 0 for num in arr]

        # Case 3: If there are no zeros, calculate product except self
        return [product // num for num in arr]  # List comprehension

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends