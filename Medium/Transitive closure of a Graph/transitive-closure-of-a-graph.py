class Solution:
    #Function to find the transitive closure of a graph.
    def transitiveClosure(self,N,graph):
        #Creating a matrix to store reachability status.
        reach=[[-1 for i in range(N)] for i in range(N)]

        #Initializing reachability matrix based on the input graph.
        for i in range(N):
            for j in range(N):
                if i == j:
                    reach[i][j] = 1
                else:
                    reach[i][j] = graph[i][j]
            
        #Applying the Floyd-Warshall algorithm to find transitive closure.
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    reach[i][j] = (reach[i][j])or(reach[i][k] and reach[k][j])
        
        #Returning the transitive closure matrix.
        return reach

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends