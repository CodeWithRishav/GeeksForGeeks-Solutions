class Solution:
   
    def find_set(self, vertex, parent):
        # Recursively find the parent node.
        if vertex != parent[vertex]:
            vertex = self.find_set(parent[vertex], parent)
        return vertex
       
    def union(self, x, y, parent, rank):
        # Merge two nodes x and y.
        x = self.find_set(x, parent)
        y = self.find_set(y, parent)
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        rank[x] += rank[y]

    def detectCycle(self, num_vertices, adjacency_list):
        # Initialize parent and rank arrays for each vertex.
        parent = [i for i in range(num_vertices)]
        rank = [1 for i in range(num_vertices)]
        visited_edges = set()

        for u in range(num_vertices):
            # Iterate through all edges of the graph.
            for v in adjacency_list[u]:
                # Skip if the edge is already visited in either direction.
                if (u, v) in visited_edges or (v, u) in visited_edges:
                    continue
                visited_edges.add((u, v))

                # Find the sets to which u and v belong.
                u_set = self.find_set(u, parent)
                v_set = self.find_set(v, parent)

                # If both vertices belong to the same set, there is a cycle.
                if u_set == v_set:
                    return 1

                # Merge the sets.
                self.union(u_set, v_set, parent, rank)
               
        # No cycle found.
        return 0


#{ 
 # Driver Code Starts

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
		ans = obj.detectCycle(V, adj)
		print(ans)
# } Driver Code Ends