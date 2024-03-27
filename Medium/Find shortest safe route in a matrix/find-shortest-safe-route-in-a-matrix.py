from typing import List
from collections import deque

class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        # code here
        if not mat or not mat[0]:
            return -1
        
        n, m = len(mat), len(mat[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
        def is_blocked(x, y):
            if mat[x][y] == 0:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                    return True
            return False
        
        queue = deque([(i, 0, 1) for i in range(n) if not is_blocked(i, 0)])
        vis = [[False for _ in range(m)] for _ in range(n)]  # Visited matrix
        
        while queue:
            x, y, dist = queue.popleft()
            if y == m - 1:
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and not is_blocked(nx, ny):
                    vis[nx][ny] = True  
                    queue.append((nx, ny, dist + 1))
        
        return -1
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        mat=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findShortestPath(mat)
        
        print(res)
        

# } Driver Code Ends