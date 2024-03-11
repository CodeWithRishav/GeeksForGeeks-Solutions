#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        # code here
        s=set()
        res=0
        for i in range(n):
            for j in range(n):
                s.add(mat2[i][j])
        for i in range(n):
            for j in range(n):
                if x-mat1[i][j] in s:
                    res+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends