class Solution:

    # checks if it's possible to pick k elements
    # with at least 'mid' difference
    def isPossible(self, arr, k, mid):
        count = 1
        last = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - last >= mid:
                count += 1
                last = arr[i]
            if count == k:
                return True

        return False

    def maxMinDiff(self, arr, k):
        # sort the array
        arr.sort()

        # define binary search range
        low = 0
        high = arr[-1] - arr[0]
        answer = 0

        # binary search to find max valid min-diff
        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(arr, k, mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        # return the maximum feasible
        # minimum difference
        return answer