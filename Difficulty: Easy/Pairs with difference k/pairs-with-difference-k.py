#User function Template for python3
class Solution:
    def countPairsWithDiffK(self,arr, k):
        # code here
        i,j,n=0,1,len(arr)
        arr.sort()
        ans=0
        while j<n:
            diff=arr[j]-arr[i]
            if diff==k:
                countI,countJ=1,1
                while i<n-1 and arr[i]==arr[i+1]:
                    countI+=1
                    i+=1
                while j<n-1 and arr[j]==arr[j+1]:
                    countJ+=1
                    j+=1
                ans+=(countI*countJ)
                i+=1
                j+=1
            elif diff<k:
                j+=1
            else:
                i+=1
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends