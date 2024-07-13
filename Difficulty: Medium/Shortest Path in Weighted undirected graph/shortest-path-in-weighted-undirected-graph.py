#User function Template for python3
from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        
        from collections import defaultdict, deque
        from heapq import heappush, heappop
        
        g = defaultdict(list)
        for frm, to, w in edges:
            g[frm].append((to, w))
            g[to].append((frm, w))
        
        q = [(0, 1)]
        costs = {1: 0}
        parents = {1: None}

        
        def build_path(cost, last):
            nonlocal parents
            q = deque()
            while last:
                q.appendleft(last)
                last = parents[last]
            q.appendleft(cost)
            return q
            
        while q:
            cost0, frm = heappop(q)
            if frm == n:
                return build_path(cost0, frm)
            for to, w in g[frm]:
                cost = cost0+w
                if to not in costs or cost < costs[to]:
                    costs[to] = cost
                    parents[to] = frm
                    heappush(q, (cost, to))
        return [-1]


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends