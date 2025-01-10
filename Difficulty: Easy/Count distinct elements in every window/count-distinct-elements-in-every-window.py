
from collections import defaultdict


class Solution:

    def countDistinct(self, arr, k):
        # Creates an empty hashmap mp
        mp = defaultdict(lambda: 0)
        n = len(arr)
        # initialize distinct element
        # count for current window
        dist_count = 0
        # Traverse the first window and store count
        # of every element in hash map
        for i in range(k):
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1

        res = []
        # Print count of first window
        res.append(dist_count)

        # Traverse through the remaining array
        for i in range(k, n):

            # Remove first element of previous window
            # If there was only one occurrence,
            # then reduce distinct count.
            if mp[arr[i - k]] == 1:
                dist_count -= 1
            mp[arr[i - k]] -= 1

            # Add new element of current window
            # If this element appears first time,
            # increment distinct element count
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1

            # Print count of current window
            res.append(dist_count)

        return res


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends