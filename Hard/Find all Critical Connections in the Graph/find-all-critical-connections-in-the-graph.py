#User function Template for python3

class Solution:
    def criticalConnections(self, v, adj):
        # code here
        def dfs(u, parent, disc, low, bridges):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            for v in adj[u]:
                if disc[v] == -1:
                    dfs(v, u, disc, low, bridges)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((min(u, v), max(u, v)))
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        disc = [-1] * v
        low = [-1] * v
        time = 0
        bridges = []
        for i in range(v):
            if disc[i] == -1:
                dfs(i, -1, disc, low, bridges)
        return sorted(bridges)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends