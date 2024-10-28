#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:

    def removeDuplicates(self, arr):
        n = len(arr)
        # create a list to keep track of whether a number has been encountered before
        dp = [0] * 100

        # create an empty list to store unique numbers
        tmp = list()

        # iterate through the input list
        for prime in arr:

            # if the number has not been encountered before, add it to the unique numbers list
            if dp[prime] == 0:
                tmp.append(prime)

                # mark the number as encountered
                dp[prime] = 1

        # create a new list to store the unique numbers in order
        result = []
        for prime in tmp:
            result.append(prime)

        # return the list of unique numbers
        return result 
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends