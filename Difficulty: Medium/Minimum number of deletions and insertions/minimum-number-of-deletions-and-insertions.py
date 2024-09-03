#User function Template for python3
class Solution:

    def minOperations(self, str1, str2):
        m = len(str1)  #length of string str1
        n = len(str2)  #length of string str2

        #creating a 2D array dp of size (m+1) x (n+1)
        #dp[i][j] represents the length of the longest common subsequence
        #of the substrings str1[0:i] and str2[0:j]
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

        #iterating through all the substrings of s1 and s2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (str1[i -
                         1] == str2[j -
                                    1]):  #if the current characters are equal
                    dp[i][j] = 1 + dp[i -
                                      1][j -
                                         1]  #incrementing the length of LCS
                else:
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )  #taking the maximum of the lengths of LCSs of substrings without the current characters

        lcslen = dp[m][
            n]  #length of the longest common subsequence of s1 and s2

        delete = m - lcslen  #number of deletions required to make s1 equal to s2
        insert = n - lcslen  #number of insertions required to make s1 equal to s2

        return delete + insert


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends