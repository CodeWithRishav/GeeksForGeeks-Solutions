class Solution :
	def palindromicPartition(self,s) :
		n = len(s)
		# Create two arrays to build the solution in bottom up manner
		#  C[i] = Minimum number of cuts needed for palindrome partitioning
		#             of substring s[0..i]
		#   P[i][j] = true if substring s[i..j] is palindrome, else false
		#   Note that C[i] is 0 if P[0][i] is true */
		C = [0]*n
		P = [[False for i in range(n)] for i in range(n)] 


		for i in range(n):
			P[i][i] = True

		for L in range(2,n+1) :
			for i in range(n-L+1):
				j = i+L-1   # set ending index
				# If L is 2, then we just need to compare two characters. Else
				# need to check two corner characters and value of P[i+1][j-1]
				if L == 2 :
					P[i][j] = (s[i] == s[j])
				else :
					P[i][j] = ((s[i] == s[j]) & P[i+1][j-1])

		for i in range(n) : 
			if P[0][i] :
				C[i] = 0
			else :
				C[i] = (1<<32)
				for j in range(i):
				    if P[j+1][i] == True and C[j]+1 < C[i] :
					    C[i] = C[j]+1

		return C[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends