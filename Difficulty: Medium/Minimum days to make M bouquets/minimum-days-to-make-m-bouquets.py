class Solution:

    def check(self, arr, k, m, days):
        bouquets = 0
        cnt = 0

        # Iterate through the bloom
        # days of the flowers
        for flower in arr:
            if flower <= days:
                cnt += 1
            else:

                # If the current bloom day count
                # is greater than days, update
                # the bouquets and reset count
                bouquets += cnt // k
                cnt = 0

        bouquets += cnt // k

        # Check if current bouquets are greater
        # than or equal to the desired
        # number of bouquets (m)
        return bouquets >= m

    def minDaysBloom(self, arr, k, m):
        lo = 0
        hi = max(arr)
        res = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if self.check(arr, k, m, mid):

                # If the current mid is valid, update the result
                # and adjust the search range
                res = mid
                hi = mid - 1
            else:

                # If the current mid is not valid, adjust the search range
                lo = mid + 1
        return res