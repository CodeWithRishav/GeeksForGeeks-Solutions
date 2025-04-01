#User function Template for python3

class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        V = len(adj)

        # initialize a visited list to keep track of visited nodes
        visited = [0] * V

        # initialize an empty list to store the DFS traversal
        values = []

        # call the dfs function to perform DFS traversal
        self.dfsRec(0, adj, visited, values)

        # return the DFS traversal list
        return values

    # DFS function to perform depth-first search
    def dfsRec(self, node, adj, visited, values):

        # mark the current node as visited
        visited[node] = 1

        # append the current node to the DFS traversal list
        values.append(node)

        # visit all the adjacent nodes of the current node
        for i in adj[node]:

            # if the adjacent node is not visited, recursively call the dfs function
            if visited[i] == 0:
                self.dfsRec(i, adj, visited, values)


#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())
        adj = []

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.dfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends