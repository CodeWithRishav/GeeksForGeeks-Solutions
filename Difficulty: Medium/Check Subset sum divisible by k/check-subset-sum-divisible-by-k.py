class Solution:

    def divisibleByK(self, arr, k):
        n = len(arr)

        if n >= k:
            return True

        dp = [False] * k

        for i in range(n):
            if dp[0]:
                return True

            temp = [False] * k

            for j in range(k):
                if dp[j]:
                    if not dp[(j + arr[i]) % k]:
                        temp[(j + arr[i]) % k] = True

            for j in range(k):
                if temp[j]:
                    dp[j] = True

            dp[arr[i] % k] = True

        return dp[0]