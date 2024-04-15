#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        ans = [0]*q
        b.sort()
        def binary_search(x):
            low , high =0, n-1
            while low <= high:
                mid = (low+high)//2
                if b[mid] > x:
                    high = mid-1
                else:
                    low = mid+1
            return low
        for i in range(0,q):
            ans[i] = binary_search(a[query[i]])
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends