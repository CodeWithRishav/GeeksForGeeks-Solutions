#User function Template for python3


class Solution:
    def findMissing(self,a,b,n,m):
    # code here
        set_b = set(b)
        
        # Initialize a list to store missing elements
        missing_elements = []
        
        # Iterate over elements of array a
        for num in a:
            # If num is not present in set_b, it's a missing element
            if num not in set_b:
                missing_elements.append(num)
        
        return missing_elements



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends