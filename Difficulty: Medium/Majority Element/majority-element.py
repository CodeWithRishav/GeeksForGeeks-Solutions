#User function template for Python 3

class Solution:

    def majorityElement(self, arr):
        n = len(arr)
        candidate = -1
        count = 0

        # Find a candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Validate the candidate
        count = 0
        for num in arr:
            if num == candidate:
                count += 1

        # If count is greater than n / 2, return the candidate; otherwise, return -1
        if count > n // 2:
            return candidate
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends