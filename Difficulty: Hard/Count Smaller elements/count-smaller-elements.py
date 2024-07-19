#User function Template for python3
from sortedcontainers import SortedList
class Solution:
    def constructLowerArray(self, arr):
        lst = SortedList()
        
        ans = [0 for i in range(len(arr))]
        
        for i in reversed(range(len(arr))):
            lst.add(arr[i])
            
            ans[i] = lst.index(arr[i])
        
        # Return the answer list
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends