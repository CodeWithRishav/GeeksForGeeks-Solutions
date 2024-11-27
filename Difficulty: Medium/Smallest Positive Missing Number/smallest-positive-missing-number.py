#User function Template for python3

class Solution:

    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)  # defining n as the length of the array

        # first separating positive and negative numbers.
        shift = self.segregate(arr)

        # shifting the array to access only positive part.
        # calling function to find result and returning it.
        return self.findMissingPositive(arr[shift:])

    # Function that puts all non-positive (0 and negative) numbers on left
    # side of arr[] and return count of such numbers.
    def segregate(self, arr):
        n = len(arr)  # defining n as the length of the array
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                # changing the position of negative numbers and 0.
                arr[i], arr[j] = arr[j], arr[i]
                # incrementing count of non-positive integers
                j += 1

        return j

    # Finding the smallest positive missing number in an array
    # that contains only positive integers.
    def findMissingPositive(self, arr):
        n = len(arr)  # defining n as the length of the array

        # marking arr[i] as visited by making arr[arr[i] - 1] negative.
        # note that 1 is subtracted because indexing starts from 0 and
        # positive numbers start from 1.
        for i in range(n):
            if abs(arr[i]) - 1 < n and arr[abs(arr[i]) - 1] > 0:
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

        for i in range(n):
            if arr[i] > 0:
                # returning the first index where value is positive.
                # 1 is added because indexing starts from 0.
                return i + 1

        return n + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends