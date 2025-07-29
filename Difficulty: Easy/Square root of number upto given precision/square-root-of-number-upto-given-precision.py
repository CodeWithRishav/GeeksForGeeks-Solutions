class Solution:

    def squareRoot(self, n, p):
        start, end = 0, n
        ans = 0.0

        # Binary search for integer part
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == n:
                ans = float(mid)
                break
            if mid * mid < n:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        # Refinement for decimal precision
        increment = 0.1
        for _ in range(p):
            while (ans + increment) * (ans + increment) <= n:
                ans += increment
            increment /= 10

        return ans