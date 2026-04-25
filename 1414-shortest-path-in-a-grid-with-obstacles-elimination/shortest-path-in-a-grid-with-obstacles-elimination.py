class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
    
        if k >= m + n - 2:
            return m + n - 2
        
        queue = [(0, 0, k, 0)]
        visited = set()
        visited.add((0, 0, k))
        
        i = 0
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while i < len(queue):
            r, c, remaining_k, steps = queue[i]
            i += 1
            
            if r == m - 1 and c == n - 1:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_k = remaining_k - grid[nr][nc]
                    
                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        queue.append((nr, nc, new_k, steps + 1))
        
        return -1