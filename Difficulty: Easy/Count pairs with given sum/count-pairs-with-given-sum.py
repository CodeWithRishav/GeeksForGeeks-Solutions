#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:

    def countPairs(self, arr, target):
        freq_map = {}
        count = 0

        for num in arr:
            # Check if the complement (target - num) exists in the map
            if target - num in freq_map:
                count += freq_map[target - num]

            # Increment the frequency of num
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        return count
       

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends