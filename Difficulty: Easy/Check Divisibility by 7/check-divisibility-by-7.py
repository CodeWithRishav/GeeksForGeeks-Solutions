class Solution:

    def isDivBy7(self, n):
        n = abs(n)

        # Ensure non-negative input

        if n == 0 or n == 7:
            return True

        while n >= 10:
            lastD = n % 10
            n //= 10
            n = abs(n - 2 * lastD)

        return n == 0 or n == 7