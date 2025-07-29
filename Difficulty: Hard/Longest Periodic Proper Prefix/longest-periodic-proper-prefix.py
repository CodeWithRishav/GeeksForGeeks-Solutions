def add(a, b, mod):
    return (a + b) % mod


# modular subtraction
def subtract(a, b, mod):
    return (a - b + mod) % mod


# modular multiplication
def multiply(a, b, mod):
    return (a * b) % mod


# get hash of substring input[left..right-1] using
# both hash bases
def getHash(preHash, power, left, right, mod):
    result = [0, 0]
    for b in range(2):
        result[b] = \
            subtract(preHash[right][b], \
                        multiply(preHash[left][b], \
                                power[right - left][b], mod), mod)
    return result


# function to compute prefix hashes and power arrays
def buildHashes(s, mod, base1, base2):
    n = len(s)
    preHash = [[0, 0] for _ in range(n + 1)]
    power = [[1, 1] for _ in range(n + 1)]

    for i in range(n):
        preHash[i + 1][0] = \
            add(multiply(preHash[i][0], base1, mod), ord(s[i]), mod)
        preHash[i + 1][1] = \
            add(multiply(preHash[i][1], base2, mod), ord(s[i]), mod)

        power[i + 1][0] = multiply(power[i][0], base1, mod)
        power[i + 1][1] = multiply(power[i][1], base2, mod)

    return preHash, power


class Solution:

    def getLongestPrefix(self, s):
        mod = 10**9 + 7
        base1 = 4441
        base2 = 7817
        n = len(s)

        preHash, power = buildHashes(s, mod, base1, base2)
        mark = [0] * (n + 1)
        maxLenPre = -1

        for len_ in range(1, n):
            if mark[len_]:
                continue

            idx = 0
            isPrefix = True

            while idx < n:
                remLen = n - idx

                # when the remaining length is smaller than p
                # refix length
                if remLen <= len_:
                    hs1 = getHash(preHash, power, idx, n, mod)
                    hs2 = getHash(preHash, power, 0, remLen, mod)
                    if hs1 != hs2:
                        isPrefix = False
                    break

                # compare next full prefix chunk with
                # original prefix
                hs1 = getHash(preHash, power, idx, idx + len_, mod)
                hs2 = getHash(preHash, power, 0, len_, mod)

                if hs1 != hs2:
                    isPrefix = False
                    break

                idx += len_

            # if valid prefix, mark all its multiples
            if isPrefix:
                for x in range(len_, n, len_):
                    mark[x] = 1
                    maxLenPre = max(maxLenPre, x)

        return maxLenPre