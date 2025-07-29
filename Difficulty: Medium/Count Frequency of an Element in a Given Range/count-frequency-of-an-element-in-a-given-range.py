class Solution:

    def freqInRange(self, arr, queries):
        indexMap = {}

        # store all indices of each value in the map
        for i, val in enumerate(arr):
            if val not in indexMap:
                indexMap[val] = []
            indexMap[val].append(i)

        result = []

        # process each query
        for l, r, x in queries:
            # if x does not exist in map, frequency is 0
            if x not in indexMap:
                result.append(0)
                continue

            ind = indexMap[x]

            # count occurrences between l and r using binary search
            left = bisect.bisect_left(ind, l)
            right = bisect.bisect_right(ind, r)

            # number of occurrences is difference of bounds
            result.append(right - left)

        return result