
class Solution:

    def isCycleUtil(self, v, adj, visited, parent):
        visited[v] = True

        for i in adj[v]:
            if not visited[i]:
                if self.isCycleUtil(i, adj, visited, v):
                    return True
            elif i != parent:
                return True
        return False

    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]  # Initialize adjacency list

        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        for u in range(V):
            if not visited[u]:
                if self.isCycleUtil(u, adj, visited, -1):
                    return True
        return False


#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends