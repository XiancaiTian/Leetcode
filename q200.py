# DFS solution
class Solution:
    """
    DFS
    start from a land, and search the 4 directions
    if be blocked by water or wall: return
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case
        if not grid: 
            return 0
        
        def dfs(i, j):
            if i < 0 or i == n_row or j < 0 or j == n_col: 
                return 
            
            elif grid[i][j] == '0': 
                return 
            
             # mark global grid as visited
            grid[i][j] = '0'
            
            # move one step at a time
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            
        n_row, n_col = len(grid), len(grid[0])
        count = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count
    
    
    
    
# BFS solution
# utilize iteration
# have a queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0 
        
        n = len(grid)
        m = len(grid[0])
        
        visited = [[0] * m for i in range (n)]
        
        def bfs(i,j):
            visited[i][j]=1
            queue = [(i,j)]
            while queue :
                # print(queue)
                point = queue.pop(0)
                i = point[0]
                j = point[1]
                if i > 0 and visited[i-1][j] == 0 and grid[i-1][j] == "1" :
                    queue.append((i-1, j ))
                    visited[i-1][j]=1
                    
                if j > 0 and visited[i][j-1] == 0 and grid[i][j-1] == "1" :
                    queue.append((i, j-1 ))
                    visited[i][j-1]=1
                    
                if i < n-1 and visited[i+1][j] == 0 and grid[i+1][j] == "1" :
                    queue.append((i+1, j ))
                    visited[i+1][j]=1
                    
                if j < m-1 and visited[i][j+1] == 0 and grid[i][j+1] == "1" :
                    queue.append((i, j+1 ))
                    visited[i][j+1]=1
                
            return
        
        count  =0 
        # bfs(0,0)
        # print(visited)
        
        for  i in range (n):
            for j in range(m):
                # print(visited)
                if grid[i][j] == "1" and  visited[i][j]==0 :
                    count +=1
                    bfs(i,j)
        
        return count 
