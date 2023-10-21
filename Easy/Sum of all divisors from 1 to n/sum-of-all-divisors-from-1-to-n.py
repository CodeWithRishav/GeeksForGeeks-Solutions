class Solution:
    def sumOfDivisors(self, N):
        sum = 0

        # Iterating from 1 to N.
        for i in range(1, N + 1):
            # Calculating and accumulating the sum of divisors.
            sum += (N // i) * i

        # Returning the sum of divisors.
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends