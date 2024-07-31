#User function Template for python3

class Solution:
   def longestCommonPrefix(self, arr):
        arr.sort()
        first  = arr[0]
        last = arr[-1]
        i = 0
        while i<len(first) and first[i]==last[i]:
            i+=1
        return first[:i] if i!=0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends