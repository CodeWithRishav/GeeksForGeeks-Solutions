MOD = 10**9 + 7
BASE1 = 4441
BASE2 = 7817


# modular arithmetic functions
def add(a, b):
    return (a + b) % MOD


def subtract(a, b):
    return (a - b + MOD) % MOD


def multiply(a, b):
    return (a * b) % MOD


# precompute prefix hash and power arrays
def buildHashes(s):
    n = len(s)
    preHash = [[0, 0] for _ in range(n + 1)]
    power = [[1, 1] for _ in range(n + 1)]

    for i in range(n):
        preHash[i + 1][0] = add(multiply(preHash[i][0], BASE1), ord(s[i]))
        preHash[i + 1][1] = add(multiply(preHash[i][1], BASE2), ord(s[i]))

        power[i + 1][0] = multiply(power[i][0], BASE1)
        power[i + 1][1] = multiply(power[i][1], BASE2)

    return preHash, power


# returns hash of substring s[left:right]
def getHash(preHash, power, left, right):
    result = [0, 0]
    for b in range(2):
        result[b] = subtract(
            preHash[right][b],
            multiply(preHash[left][b], power[right - left][b]))
    return result


class Solution:

    def getCount(self, freqMap):
        total = 0
        for freq in freqMap.values():
            total += (freq * (freq - 1)) // 2
        return total

    def countPairs(self, arr):
        n = len(arr)
        m = len(arr[0])

        wildcardFreq = {}
        fullFreq = {}

        for word in arr:
            preHash, power = buildHashes(word)

            # consider each position as the differing index
            for i in range(m):
                left = getHash(preHash, power, 0, i)
                right = getHash(preHash, power, i + 1, m)

                overall = tuple(left + right)
                wildcardFreq[overall] = wildcardFreq.get(overall, 0) + 1

            fullHash = tuple(getHash(preHash, power, 0, m))
            fullFreq[fullHash] = fullFreq.get(fullHash, 0) + 1

        totalPairs = self.getCount(wildcardFreq)
        duplicate = self.getCount(fullFreq) * m

        return totalPairs - duplicate