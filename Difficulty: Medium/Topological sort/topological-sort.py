class Solution:

    def topoSortUtil(self, v, adj, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all adjacent vertices
        for i in adj[v]:
            if not visited[i]:
                self.topoSortUtil(i, adj, visited, stack)

        # Push current vertex to stack which stores the result
        stack.append(v)

    def topoSort(self, V, edges):
        # Stack to store the result
        stack = []
        visited = [False] * V
        adj = [[] for _ in range(V)]

        for it in edges:
            adj[it[0]].append(it[1])

        # Call the recursive helper function to store
        # Topological Sort starting from all vertices one by one
        for i in range(V):
            if not visited[i]:
                self.topoSortUtil(i, adj, visited, stack)

        # Reverse stack to get the correct topological order
        return stack[::-1]



#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        x = V
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, x, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends