# DFS solution
# go over every point
# if visited: label as '#'
# utilize rescursion
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
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
