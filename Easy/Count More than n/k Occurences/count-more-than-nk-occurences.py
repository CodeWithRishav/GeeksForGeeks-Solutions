#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        di = {}
        co = []
        res = 0
        for i in arr:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
            # if di[i] > (n/k) and i not in co:
            #     co.append(i)
            #     res += 1
        for i in di:
            if di[i] > (n/k):
                res+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends