#User function Template for python3
class Solution:
    # Function to calculate (x^y) % p using binary exponentiation
    def power(self, x, y, p):
        result = 1
        x = x % p  # Ensure x is within mod range

        while y > 0:
            # If y is odd, multiply x with the result
            if (y & 1) == 1:
                result = (result * x) % p
            # y = y // 2
            y = y >> 1
            # x = x^2 % p
            x = (x * x) % p
        return result

    # Function to count the number of ways to split array into two groups such that each group has equal XOR value
    def countgroup(self, arr):
        mod = 1000000007  # Define the mod value
        n = len(arr)  # Get the size of the input array
        xs = 0  # Initialize XOR sum

        # Compute the XOR of the entire array
        for i in range(n):
            xs ^= arr[i]

        # We can split only if the XOR of the entire array is 0
        if xs == 0:
            # If XOR of the whole array is 0, calculate 2^(n-1) - 1
            ans = self.power(2, n - 1, mod) - 1
            if ans < 0:
                ans += mod  # Ensure the answer is non-negative
            return ans

        return 0  # If XOR isn't 0, we cannot split the array



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends