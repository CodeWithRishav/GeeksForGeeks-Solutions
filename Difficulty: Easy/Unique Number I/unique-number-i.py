class Solution:
    def findUnique(self, arr):
        # code here 
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]] = d[arr[i]]+1
        for k,v in d.items():
            if v==1:
                return k


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findUnique(arr)
        print(ans)
        print("~")
# } Driver Code Ends