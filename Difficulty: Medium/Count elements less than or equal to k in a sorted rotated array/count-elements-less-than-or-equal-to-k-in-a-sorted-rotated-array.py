class Solution:

    def findMinIndex(self, arr, low, high):
        if high < low:
            return 0
        if high == low:
            return low

        mid = (low + high) // 2

        if mid < high and arr[mid + 1] < arr[mid]:
            return mid + 1
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid

        if arr[high] > arr[mid]:
            return self.findMinIndex(arr, low, mid - 1)
        return self.findMinIndex(arr, mid + 1, high)

    def binary_search(self, arr, l, h, x):
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] <= x:
                l = mid + 1
            else:
                h = mid - 1
        return h

    def countEleLessThanOrEqual(self, arr, x):
        n = len(arr)
        min_index = self.findMinIndex(arr, 0, n - 1)

        if x <= arr[-1]:
            return self.binary_search(arr, min_index, n - 1, x) + 1 - min_index
        if min_index - 1 >= 0 and x <= arr[min_index - 1]:
            return n - min_index + self.binary_search(arr, 0, min_index - 1,
                                                      x) + 1
        return n