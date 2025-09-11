class Solution:

    def minJumps(self, arr):
        n = len(arr)

        # Return -1 if not possible to jump
        if arr[0] == 0:
            return -1

        # Stores the maximal reachable index
        maxReach = 0

        # Stores the number of steps we can still take
        currReach = 0

        # Stores the number of jumps needed
        # to reach current reachable index
        jump = 0

        # Start traversing array
        for i in range(n):
            maxReach = max(maxReach, i + arr[i])

            # If we can reach last index by jumping
            # from current position return Jump + 1
            if maxReach >= n - 1:
                return jump + 1

            # Increment the Jump as we reached the
            # Current Reachable index
            if i == currReach:

                # If Max reach is same as current index
                # then we can not jump further
                if i == maxReach:
                    return -1

                # If Max reach > current index then increment
                # jump and update current reachable index
                else:
                    jump += 1
                    currReach = maxReach

        return -1