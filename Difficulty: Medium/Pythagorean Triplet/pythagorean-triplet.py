class Solution:

    def pythagoreanTriplet(self, arr):
        n = len(arr)
        maxEle = 0
        for ele in arr:
            maxEle = max(maxEle, ele)

        # Visited array to mark the elements
        vis = [False] * (maxEle + 1)

        # Marking each element of input array
        for ele in arr:
            vis[ele] = True

        # Iterate for all possible a
        for a in range(1, maxEle + 1):

            # If a is not there
            if not vis[a]:
                continue

            # Iterate for all possible b
            for b in range(1, maxEle + 1):

                # If b is not there
                if not vis[b]:
                    continue

                # calculate c value to form a pythagorean triplet
                c = int(math.sqrt(a * a + b * b))

                # If c^2 is not a perfect square or c exceeds the
                # maximum value
                if (c * c) != (a * a + b * b) or c > maxEle:
                    continue

                # If there exists c in the original array,
                # we have found the triplet
                if vis[c]:
                    return True

        return False