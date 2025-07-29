class Solution:

    def primeFactors(self, n):
        factors = []

        # Count the number of 2's that divide n
        while n % 2 == 0:
            factors.append(2)
            n //= 2

        # n must be odd at this point
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i

        # If n is a prime number greater than 2
        if n > 2:
            factors.append(n)
        return factors