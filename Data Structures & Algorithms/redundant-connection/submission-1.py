class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in edges:
            if u in adj and v in adj:
                visited = set()
                visited.add(u)
                q = deque([u])
                while q:
                    curr = q.popleft()
                    if curr == v:
                        return [u, v]
                    for nei in adj[curr]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            adj[u].append(v)
            adj[v].append(u)
        return [0]
