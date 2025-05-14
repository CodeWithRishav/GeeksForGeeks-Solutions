class Solution:

    def countAndSay(self, n):
        if n == 1:
            return "1"

        curr = "1"

        # Start from the second term, build every term
        # terms using the previous term
        for i in range(2, n + 1):
            next_str = ""
            cnt = 1

            for j in range(1, len(curr)):

                # If same as previous, then increment
                # count
                if curr[j] == curr[j - 1]:
                    cnt += 1

                # If different process the previous
                # character and its count and reset
                # count for the current character
                else:
                    next_str += str(cnt) + curr[j - 1]
                    cnt = 1

            next_str += str(cnt) + curr[-1]
            curr = next_str

        return curr

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends