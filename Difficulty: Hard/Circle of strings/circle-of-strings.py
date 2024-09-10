#User function Template for python3

class Solution:
    # Helper function to perform DFS on the graph
    def dfs(self, v, visited, adj):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                self.dfs(u, visited, adj)

    # Helper function to check if all non-zero degree vertices are strongly connected
    def isStronglyConnected(self, adj, revAdj, degree):
        n = 26  # Since there are only 26 lowercase letters

        # Find the first vertex with a non-zero degree
        start = -1
        for i in range(n):
            if degree[i] > 0:
                start = i
                break

        # If no vertex has edges, it's trivially a circle
        if start == -1:
            return True

        # Check connectivity in the original graph
        visited = [False] * n
        self.dfs(start, visited, adj)

        # Ensure all vertices with non-zero degree are visited
        for i in range(n):
            if degree[i] > 0 and not visited[i]:
                return False

        # Check connectivity in the reverse graph
        visited = [False] * n  # Reset the visited array
        self.dfs(start, visited, revAdj)

        # Ensure all vertices with non-zero degree are visited in the reverse graph as well
        for i in range(n):
            if degree[i] > 0 and not visited[i]:
                return False

        return True

    def isCircle(self, arr):
        n = len(arr)
        adj = [[] for _ in range(26)]       # Adjacency list for graph
        revAdj = [[] for _ in range(26)]    # Reverse adjacency list for reverse graph
        inDeg = [0] * 26                    # In-degree array
        outDeg = [0] * 26                   # Out-degree array

        # Build the graph
        for s in arr:
            u = ord(s[0]) - ord('a')  # First character
            v = ord(s[-1]) - ord('a')  # Last character
            adj[u].append(v)           # Add edge from u to v
            revAdj[v].append(u)        # Add reverse edge from v to u
            outDeg[u] += 1             # Increment out-degree of u
            inDeg[v] += 1              # Increment in-degree of v

        # Check if in-degree and out-degree of each vertex are equal
        for i in range(26):
            if inDeg[i] != outDeg[i]:
                return 0  # If in-degree and out-degree are not equal, can't form a circle

        # Check if the graph is strongly connected for vertices involved in the chain
        if not self.isStronglyConnected(adj, revAdj, inDeg):
            return 0  # If the graph is not strongly connected, can't form a circle

        return 1  # The strings can be chained to form a circle


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends