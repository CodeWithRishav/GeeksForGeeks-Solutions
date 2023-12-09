class Solution:
    # Simple prime factorization using trial division:
    def factorize(self, n0):
        result = []
        n = n0
        if n < 2: return result
        if (n & 1) == 0:
            k = (n & -n).bit_length() - 1
            result.append((2, k))
            n = n >> k
        p = 3
        while p*p <= n:
            q, r = divmod(n, p)
            k = 0
            while r == 0:
                n = q
                k += 1
                q, r = divmod(n, p)
            if k > 0:
                result.append((p, k))
            p += 2
        if n > 1: result.append((n, 1))
        return result

    # Function to check if a number is a Smith number
    def smithNum(self, n):

        # Function to calculate the digit sum of a number
        dsum = lambda n: sum(map(int, str(n)))

        # Perform prime factorization of the given number
        pf = self.factorize(n)

        # Check if the number is composite (has more than 1 prime factor)
        if len(pf) == 0 or len(pf) == 1 and pf[0][1] == 1:
            return 0    # not composite
        
        # Calculate the digit sum of the original number
        original_sum = dsum(n)
        
        # Calculate the digit sum of the prime factors multiplied by their exponents
        smith_sum = sum(dsum(p) * k for p, k in pf)
        
        # Check if the original sum is equal to the smith sum
        return int(original_sum == smith_sum)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends