from typing import List
class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        
        def is_valid(x, y):
            return 0 <= x < len(m) and 0 <= y < len(m[0]) and m[x][y] == 1
        
        def backtrack(x, y, path):
            if x == len(m) - 1 and y == len(m[0]) - 1:
                result.append(path)
                return
            for dx, dy, direction in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    m[nx][ny] = 0  
                    backtrack(nx, ny, path + direction)
                    m[nx][ny] = 1  
        
        result = []
        if m[0][0] == 1:  
            m[0][0] = 0  
            backtrack(0, 0, '')
            m[0][0] = 1  
        return sorted(result)


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends