#User function Template for python3

class Solution:

    def nCr(self, n, r):
        # Edge case where r is greater than n
        if r > n:
            return 0

        sum = 1

        # Calculate the value using
        # the binomial coefficient formula
        for i in range(1, r + 1):
            sum = sum * (n - r + i) // i

        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends