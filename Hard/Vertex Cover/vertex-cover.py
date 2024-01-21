from typing import List


class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        def solve(edges):
            if len(edges)==0:
                return 0
            ed0=[]
            ed1=[]
            for i in edges:
                if not(i[0]==edges[0][0] or i[1]==edges[0][0]):
                    ed0.append(i)
                if not(i[0]==edges[0][1] or i[1]==edges[0][1]):
                    ed1.append(i)
            ans0=1+solve(ed0)
            ans1=1+solve(ed1)
            return min(ans0,ans1)
            
        return solve(edges)
        



#{ 
 # Driver Code Starts
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
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends