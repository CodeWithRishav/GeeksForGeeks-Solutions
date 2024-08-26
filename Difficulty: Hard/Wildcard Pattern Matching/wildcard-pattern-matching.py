# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        m, n = len(pattern), len(string)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True
        for i in range(1, m + 1):
            if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and pattern[i - 1] == string[j - 1]
        
        return 1 if dp[m][n] else 0



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends