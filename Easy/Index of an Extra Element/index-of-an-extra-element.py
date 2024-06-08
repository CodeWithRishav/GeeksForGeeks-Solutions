class Solution:
    def findExtra(self,n,a,b):
        l = 0
        r = n-2
        
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == b[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends