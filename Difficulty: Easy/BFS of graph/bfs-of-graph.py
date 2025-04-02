#User function Template for python3
class Solution:
    from collections import deque
    def bfs(self, adj):
        visited=set([0])
        result=[]
        queue=self.deque([0])
        while queue:
            node=queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends