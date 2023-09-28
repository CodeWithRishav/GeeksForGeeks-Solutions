class Solution:
    def find(self, arr, n, x):
        ans = [-1, -1]

        # Find the first occurrence of x
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                ans[0] = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        # Find the last occurrence of x
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                ans[1] = mid
                left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return ans

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends