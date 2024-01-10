class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Creating a dictionary to store the remainder and its corresponding index
		um = {}
		#Creating an empty list to store the remainder of each subarray sum
		mod_arr = []
		#Initializing the maximum length of subarray to 0
		maxx = 0
		#Initializing the current sum to 0
		curr_sum = 0
		
		#Calculating the remainder of each subarray sum and storing it in mod_arr
		for i in range(n) :
		    curr_sum += arr[i]
		    mod_arr.append(((curr_sum % k) + k) % k)
		
		#Iterating through mod_arr to find the maximum length of subarray with remainder 0
		#or the maximum length between two indices having the same remainder
		for i in range(n):
		    if mod_arr[i] ==0 :
		        maxx = i+1
		    elif mod_arr[i] not in um :
		        um[mod_arr[i]]=i
		    elif maxx < i-um[mod_arr[i]] :
		        maxx = i-um[mod_arr[i]]
		return maxx



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends