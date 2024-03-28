#User function Template for python3

from typing import List
import heapq

class Solution:
    
    def findCity(self, n: int, m: int, edges: list, distanceThreshold: int) -> int:
        graph = {i: [] for i in range(n)}
        for src, dest, cost in edges:
            graph[src].append((dest, cost))
            graph[dest].append((src, cost))
        
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            
            while heap:
                d, current = heapq.heappop(heap)
                if d > dist[current]:
                    continue
                
                for neighbor, weight in graph[current]:
                    distance = d + weight
                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))
            return dist
        
        min_neighbors = n
        city = -1
        for i in range(n):
            reachable_cities = sum(1 for j in dijkstra(i) if j <= distanceThreshold)
            reachable_cities -= 1
            if reachable_cities < min_neighbors or (reachable_cities == min_neighbors and i > city):
                min_neighbors = reachable_cities
                city = i
                
        return city


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends