class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n): 
        
        #using set to store the prefix sum which has appeared already.
        s = set() 
     
        sum = 0
        #iterating over the array.
        for i in range(n): 
            #storing prefix sum.
            sum += arr[i] 
      
            #if prefix sum is 0 or if it is already present in set then it is
    		#repeated which means there is a subarray whose summation was 0,
    		#so we return true.
            if sum == 0 or sum in s: 
                return True
                
            #storing every prefix sum obtained in set.
            s.add(sum) 
        
        #returning false if we don't get any subarray with 0 sum.      
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends