
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list) 
        

        for u, v, p in flights:
            adj[u].append((v, p))
            
        
        prices = [float('inf')] * n
        prices[src] = 0
        queue = deque([(src, 0)])
        stops = 0
        
        while queue and stops <= k:
            level_size = len(queue)
            for _ in range(level_size):
                curr_city, curr_cost = queue.popleft()
                for neighbor, price in adj[curr_city]:
                    new_cost = curr_cost + price
                    if new_cost < prices[neighbor]:
                        prices[neighbor] = new_cost
                        queue.append((neighbor, new_cost))
            stops += 1
            
        return prices[dst] if prices[dst] != float('inf') else -1