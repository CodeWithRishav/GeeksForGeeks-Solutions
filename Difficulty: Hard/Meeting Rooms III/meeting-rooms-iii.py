#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq


# } Driver Code Ends

#User function Template for python3
class Solution:

    def mostBooked(self, n, meetings):
        cnt = [0] * n  # Count of meetings per room
        # Min-heap for occupied rooms: (end time, room number)
        occ = []
        # Min-heap for available rooms: room numbers
        avail = list(range(n))
        heapq.heapify(avail)

        # Sort meetings by start time
        meetings.sort()

        for m in meetings:
            s, e = m

            # Release rooms that have become available by time s
            while occ and occ[0][0] <= s:
                end_time, room = heapq.heappop(occ)
                heapq.heappush(avail, room)

            if avail:
                # Assign to the smallest available room
                r = heapq.heappop(avail)
                heapq.heappush(occ, (e, r))
                cnt[r] += 1
            else:
                # All rooms are occupied; assign to the room that becomes free earliest
                t, r = heapq.heappop(occ)
                heapq.heappush(occ, (t + (e - s), r))
                cnt[r] += 1

        # Find the room with the maximum number of meetings
        maxCnt = 0
        res = 0
        for i in range(n):
            if cnt[i] > maxCnt:
                maxCnt = cnt[i]
                res = i

        return res


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    it = iter(input)
    t = int(next(it))
    while t > 0:
        t -= 1
        n = int(next(it))
        m = int(next(it))
        meetings = []
        for _ in range(m):
            s = int(next(it))
            e = int(next(it))
            meetings.append([s, e])
        sol = Solution()
        res = sol.mostBooked(n, meetings)
        print(res)
        print("~")
# } Driver Code Ends