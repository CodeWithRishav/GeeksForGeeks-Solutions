class Solution:
    def canPair(self, nums, k):
        # Code here
        mydict=dict()
        for x in range(k):
            mydict[x]=0
        for x in nums:
            z=x%k
            mydict[z]+=1
#         print(mydict)
        for x in range(k):
          #  print(x)
            if x==0:
                if mydict[x]%2!=0:
                    return False
            else:
                 if (mydict.get(x)+mydict.get(k-x))%2!=0:
                     return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends