#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:

    def totalCount(self, k, arr):
        count = 0

        # Iterating over all the elements
        for num in arr:
            # If element is divisible by k, add quotient to count
            if num % k == 0:
                count += num // k
            else:
                # If not divisible, add quotient + 1 to count
                count += (num // k + 1)
            # Increase count by 1 if element is 0
            if num == 0:
                count += 1

        # Returning total count
        return count
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
        res = ob.totalCount(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends