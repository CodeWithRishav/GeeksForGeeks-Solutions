class Solution:
    # ---------- power(a,n) mod m – 64-bit safe ----------
    def modPow(self, a, n, mod):
        if mod == 1:
            return 0
        res, p = 1, a % mod
        while n:
            if n & 1:
                res = (res * p) % mod
            p = (p * p) % mod
            n >>= 1
        return res

    def countBeautifulStrings(self, queries):
        if not queries:  # ? tiny guard, avoids max([]) ValueError
            return []

        mx = max(queries)

        # ---------- parameters ----------
        MOD = 1_000_000_007
        N = mx + 2

        # ---------- DP tables ----------
        dp = [[0] * N for _ in range(N)]
        pref = [[0] * N for _ in range(N)]
        pre = [[0] * N for _ in range(N)]

        dp[0][0] = self.modPow(25, MOD - 2, MOD) * 26 % MOD

        ten = [1, 10, 100, 1000, 10000]
        for i in range(1, mx + 1):
            pref[i][0] = dp[0][0]

        # ---------- main DP ----------
        for i in range(1, mx + 1):
            for j in range(1, mx + 1):
                for k in range(1, 5):
                    if j - k - 1 < 0:
                        continue
                    x = max(i - ten[k - 1] + 1, 0)
                    y = max(i - ten[k] + 1, 0)
                    add = (pref[x][j - k - 1] - pref[y][j - k - 1] + MOD) % MOD
                    dp[i][j] = (dp[i][j] + add * 25) % MOD
                pref[i + 1][j] = (pref[i][j] + dp[i][j]) % MOD

        # ---------- 2-D prefix for queries ----------
        for i in range(1, mx + 1):
            pre[i][1] = dp[i][1]
            for j in range(2, i):
                pre[i][j] = (pre[i][j - 1] + dp[i][j]) % MOD

        # ---------- answers ----------
        ans = []
        for x in queries:
            ans.append(pre[x][x - 1])
        return ans