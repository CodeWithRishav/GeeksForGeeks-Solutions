#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def kadane(arr):

    max_so_far = 0
    max_ending_here = 0
    n = len(arr)
    for i in range(0, n):
        #Storing max sum till current index.
        max_ending_here = max_ending_here + arr[i]

        #If max sum till current index is negative, we update it to 0.
        if (max_ending_here < 0):
            max_ending_here = 0

        #Storing the max sum so far.
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far


#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    n = len(arr)
    count = 0
    maxx = -sys.maxsize - 1
    for i in range(0, n):
        #Storing the maximum element in the array.
        if (arr[i] > maxx):
            maxx = arr[i]
        #Counting total number of negative numbers in the array.
        if (arr[i] < 0):
            count = count + 1

    if (count == n):
        return maxx

#Case 1:We get the maximum sum using standard Kadane's algorithm.
    max_kadane = kadane(arr)

    #Case 2:We now find the maximum sum that includes corner elements.
    max_wrap = 0
    for i in range(0, n):
        #Calculating total sum of array elements.
        max_wrap += arr[i]
        #Inverting the sign of array elements.
        arr[i] = -arr[i]


#Maximum sum with corner elements will be:
#Total sum of array elements-(-max subarray sum after changing
#sign of array elements).
    max_wrap = max_wrap + kadane(arr)

    #The maximum circular sum will be maximum of two sums.
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends