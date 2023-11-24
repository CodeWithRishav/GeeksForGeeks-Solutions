#User function Template for python3

#User function Template for python3
class Solution:

    def nthRowOfPascalTriangle(self,n):
        # code here
        ans = [[1], [1,1]]
        if n == 1:
            return ans[0]
            
        elif n == 2:
            return ans[1]
            
        else:
            
            k = 3
            while k <= n:
                a = [1]*k
                a1 = ans[-1]
                
                for i in range(1, k-1):
                    a[i] = a1[i-1] + a1[i]
                    a[i] = a[i]%(1000000007)
                    
                k += 1
                ans.append(a)
                
        return ans[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends