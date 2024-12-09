#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:

    # Function to insert new interval into existing intervals list.
    def insertInterval(self, intervals, newInterval):
        ans = []
        i = 0
        n = len(intervals)
        # Appending intervals that come before the new interval.
        while i < n and newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
            i += 1

        # Merging intervals that overlap with the new interval.
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ans.append(newInterval)

        # Appending remaining intervals after the new interval.
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends