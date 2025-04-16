#User function template for Python

class Solution:

    #Function to find the shortest distance between any two nodes in the graph.
    def floydWarshall(self, dist):
        V = len(dist)

        # Add all vertices one by one to
        # the set of intermediate vertices.
        for k in range(V):

            # Pick all vertices as source one by one
            for i in range(V):

                # Pick all vertices as destination
                # for the above picked source
                for j in range(V):

                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]

                    if dist[i][k] != 100000000 and dist[k][
                            j] != 100000000 and dist[i][
                                j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.floydWarshall(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends