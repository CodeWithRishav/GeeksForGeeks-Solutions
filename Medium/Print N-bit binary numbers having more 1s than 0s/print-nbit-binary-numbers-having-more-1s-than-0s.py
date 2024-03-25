#User function Template for python3
class Solution:
    def NBitBinary(self, n):
        # code here
        ans = []
        def solve(temp,ln,zeros,ones):
            if ln == n:
                if ones>=zeros:
                    ans.append(temp)
                return
            if ones>=zeros:
                solve(temp+"1",ln+1,zeros,ones+1)
                solve(temp+"0",ln+1,zeros+1,ones)
         
        solve("1",1,0,1)
        ans.sort(reverse=True)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends