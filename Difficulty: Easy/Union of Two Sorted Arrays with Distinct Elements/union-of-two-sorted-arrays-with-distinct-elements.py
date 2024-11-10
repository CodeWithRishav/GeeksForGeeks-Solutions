#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        res = []
        i = j = 0
        m,n = len(a),len(b)
        while i<m and j<n:
            if a[i]<b[j]:
                res.append(a[i])
                i += 1
            elif b[j]<a[i]:
                res.append(b[j])
                j += 1
            else:
                res.append(a[i])
                i += 1
                j += 1
        if i<m:
            res.extend(a[i:])
        if j<n:
            res.extend(b[j:])
        return res

        # code here 

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends