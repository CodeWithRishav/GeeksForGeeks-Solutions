#User function Template for python3
class Solution:

    def kthMissing(self, arr, k):
        lo = 0
        hi = len(arr) - 1
        res = len(arr) + k

        # Binary Search for index where arr[i] > (i + k)
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] > mid + k:
                res = mid + k
                hi = mid - 1
            else:
                lo = mid + 1

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends