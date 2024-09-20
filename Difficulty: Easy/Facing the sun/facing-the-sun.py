#User function Template for python3

class Solution:
    # Returns count of buildings that can see the sunlight
    def countBuildings(self, height):
        if not height:
            return 0

        max_height = float('-inf')
        count = 0

        for h in height:
            if h > max_height:
                count += 1
                max_height = h

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends