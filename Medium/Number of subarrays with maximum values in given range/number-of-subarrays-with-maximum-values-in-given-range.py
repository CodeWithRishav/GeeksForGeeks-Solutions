class Solution:
    def countSubarrys(self, n): 
      
        return n * (n + 1) // 2
      
       
    # function to count the 
    # number of sub-arrays with 
    # maximum greater then 
    # L and less then R. 
    def countSubarrays(self,a,n,L,R): 
      
        res = 0
       
        # exc is going to store 
        # count of elements 
        # smaller than L in  
        # current valid subarray. 
        # inc is going to store 
        # count of elements 
        # smaller than or equal to R. 
        exc = 0
        inc = 0
       
        # traverse through all 
        # elements of the array 
        for i in range(n): 
       
            # If the element is 
            # greater than R, 
            # add current value 
            # to result and reset 
            # values of exc and inc. 
            if (a[i] > R): 
                  
                res =res + (self.countSubarrys(inc) - self.countSubarrys(exc)) 
                inc = 0
                exc = 0
              
       
            # if it is less than L, 
            # then it is included 
            # in the sub-arrays 
            elif (a[i] < L):  
                exc=exc + 1
                inc=inc + 1
              
       
            # if >= L and <= R, then count of 
            # subarrays formed by previous chunk 
            # of elements formed by only smaller 
            # elements is reduced from result. 
            else:  
                  
                res =res - self.countSubarrys(exc) 
                exc = 0
                inc=inc + 1
       
        # Update result. 
        res =res + (self.countSubarrys(inc) - self.countSubarrys(exc)) 
       
        # returns the count of sub-arrays 
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends