
class Solution:

    def constructadj(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        return adj

    def isCycle(self, V, edges):
        adj = self.constructadj(V, edges)
        in_degree = [0] * V
        queue = deque()
        visited = 0

        for u in range(V):
            for v in adj[u]:
                in_degree[v] += 1

        for u in range(V):
            if in_degree[u] == 0:
                queue.append(u)

        while queue:
            u = queue.popleft()
            visited += 1
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return visited != V


#{ 
 # Driver Code Starts
from collections import deque


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


if __name__ == "__main__":
    main()

# } Driver Code Ends