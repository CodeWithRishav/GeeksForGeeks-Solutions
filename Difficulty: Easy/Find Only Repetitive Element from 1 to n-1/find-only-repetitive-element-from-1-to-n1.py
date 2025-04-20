#User function Template for python3
class Solution:

    def findDuplicate(self, arr):
        n = len(arr)
        res = 0

        # XOR all numbers from 1 to n-1 and
        # elements in the array
        for i in range(n - 1):
            res = res ^ (i + 1) ^ arr[i]

        # XOR the last element in the array
        res = res ^ arr[n - 1]

        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends