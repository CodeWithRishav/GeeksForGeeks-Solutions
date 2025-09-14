class Solution:

    def startStation(self, gas, cost):
        n = len(gas)

        # Variables to track total and current remaining gas
        totalGas = 0
        currGas = 0
        startIdx = 0

        # Traverse through each station to calculate remaining
        # gas in the tank, and total gas
        for i in range(n):
            currGas += gas[i] - cost[i]
            totalGas += gas[i] - cost[i]

            # If currGas is negative, circular tour can't
            # start with this index, so update it to next one
            if currGas < 0:
                currGas = 0
                startIdx = i + 1

        # No solution exists
        if totalGas < 0:
            return -1

        return startIdx