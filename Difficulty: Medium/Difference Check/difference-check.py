class Solution:
    # Convert "HH:MM:SS" to total seconds since midnight
    def toSeconds(self, time: str) -> int:
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        return h * 3600 + m * 60 + s

    def minDifference(self, arr: list[str]) -> int:
        total_sec = 24 * 3600

        # Boolean array to mark seen seconds (size = 86400)
        seen = [False] * total_sec

        n = len(arr)

        # Mark all seconds in the seen array, return 0 on duplicate
        for i in range(n):
            sec = self.toSeconds(arr[i])
            if seen[sec]:
                return 0
            seen[sec] = True

        first = -1
        last = -1
        prev = -1
        min_diff = float('inf')

        # Finding minimum difference between adjacent times
        for i in range(total_sec):
            if not seen[i]:
                continue
            if prev != -1:
                min_diff = min(min_diff, i - prev)
            else:
                first = i
            prev = i
            last = i

        # Wrap-around difference between last and first
        wrap = first + total_sec - last
        min_diff = min(min_diff, wrap)

        return min_diff