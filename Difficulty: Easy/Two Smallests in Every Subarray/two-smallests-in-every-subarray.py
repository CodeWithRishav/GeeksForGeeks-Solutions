class Solution:
    def pairWithMaxSum(self, arr):
        if len(arr) < 2: return -1
        
        ans = 0
        
        l = 0
        
        for r in arr:
            ans = max(ans, l+r)
            
            if r < l:
                l = r
            else:
                l = r
            
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends