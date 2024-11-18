#User function Template for python3

def reverse(arr,l,r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
        
    
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D):
        #Your code here
        N = len(A)
        if D == 0:
            return A
        if D > N:
            D = D%N
        
        reverse(A,0,D-1)
        reverse(A,D,N-1)
        reverse(A,0,N-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends