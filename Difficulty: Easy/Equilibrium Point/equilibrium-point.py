# User function Template for python3

class Solution:

    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        n = len(arr)
        #We store the sum of all array elements.
        sum = 0
        for i in range(0, n):
            sum += arr[i]

        #sum2 is used to store prefix sum.
        sum2 = 0

        for i in range(0, n, +1):

            #Leaving out the value of current element from suffix sum.
            sum -= arr[i]

            #Checking if suffix and prefix sums are same.
            if sum2 == sum:
                #returning the index or equilibrium point.
                return i

            #Adding the value of current element to prefix sum.
            sum2 += arr[i]

        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends