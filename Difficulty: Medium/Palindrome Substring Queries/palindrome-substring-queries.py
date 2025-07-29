def buildRollingHash(string, base1, base2, mod):
    n = len(string)
    preHash = [[0, 0] for _ in range(n + 1)]
    power = [[1, 1] for _ in range(n + 1)]

    for i in range(n):
        preHash[i + 1][0] =\
            (preHash[i][0] * base1 + ord(string[i])) % mod
        preHash[i + 1][1] = \
            (preHash[i][1] * base2 + ord(string[i])) % mod

        power[i + 1][0] = \
            (power[i][0] * base1) % mod
        power[i + 1][1] = \
            (power[i][1] * base2) % mod

    return preHash, power


def getHash(preHash, power, left, right, mod):
    return [(preHash[right][k] -
             preHash[left][k] * power[right - left][k] % mod + mod) % mod
            for k in range(2)]


class Solution:

    def palQueries(self, s, queries):
        mod = int(1e9 + 7)
        base1 = 4441
        base2 = 7817
        n = len(s)
        revS = s[::-1]

        # build hashes for original and reversed strings
        preHashF, powerF = \
            buildRollingHash(s, base1, base2, mod)
        preHashR, powerR = \
            buildRollingHash(revS, base1, base2, mod)

        result = []

        for left, right in queries:
            # get hash of s[left...right]
            h1 = getHash(preHashF, powerF, left, right + 1, mod)

            # map to reversed string: revS[n-1-right ... n-1-left]
            revLeft = n - 1 - right
            revRight = n - left
            h2 = getHash(preHashR, powerR, revLeft, revRight, mod)

            result.append(1 if h1 == h2 else 0)

        return result