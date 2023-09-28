class Solution:
    def duplicates(self, arr, n): 
    	# First check all the values that are 
    	# present in an array then go to that 
    	# values as indexes and increment by 
    	# the size of array 
    	for i in range(0, n): 
    		index = arr[i] % n 
    		arr[index] += n 
    
    	# Now check which value 
    	# exists more 
    	# than once by dividing 
    	# with the size 
    	# of array 
    	flag=False
    	res = []
    	for i in range(0,n): 
    		if (arr[i]//n) > 1: 
    			res.append(i)
    			flag=True
    	
    	if flag==False:
    	    res.append(-1)
    	return res
	    
#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends