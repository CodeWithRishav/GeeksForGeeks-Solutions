#User function Template for python3

import math
import bisect
class Solution:    
    def countPairs(self,arr, n): 
        minimum=math.inf
        maximum=-math.inf
        max_count=0
        for i in range(n):
            arr[i]=arr[i]*i
            if arr[i]>=maximum:
                maximum=arr[i]
            if arr[i]<=minimum:
                minimum=arr[i]
                
        max_count=arr.count(maximum)    
        
        total=0
        countx=0
        for i in range(n):
            if arr[i]==minimum:
                if countx>0:
                    list1.remove(arr[i])
            elif arr[i]==maximum:
                max_count-=1
                total+=(n-1-i-max_count)
                if countx>0:
                    list1.remove(arr[i])
            else:
                if countx==0:
                    list1=sorted(arr[i+1:])
                    bisect.insort(list1,arr[i])
                    countx+=1
                    
                indexz=bisect.bisect_left(list1,arr[i])
                list1.remove(arr[i])
                total+=indexz
            
        return total


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends