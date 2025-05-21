class Solution(object):

    def kthSmallest(self, m, n, k):
        l = 1
        r = m * n

        # binary search until left pointer is less than right pointer
        while (l < r):

            # calculate mid value
            mid = (l + r) // 2
            cnt = 0
            for i in range(1, m + 1):

                # calculate count by finding minimum of mid divided by i and n
                cnt += min(mid // i, n)

                # if count is less than k, move left pointer to mid+1
            if cnt < k:
                l = mid + 1
            else:
                r = mid

        # return left pointer as the kth number
        return l