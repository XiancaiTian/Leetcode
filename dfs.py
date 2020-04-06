## LEETCODE 200
# concept: start from a island, dfs and marked the island

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (i>=m) or (j >=n) or (i < 0) or (j < 0) or (grid[i][j]!='1'):
                return
            if grid[i][j]!='0':
                grid[i][j] = 'X'
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
                
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count = count + 1
                    dfs(i,j)
                    
        return count


## LEETCODE 286
# concept: start from a gate, dfs and marked the INF
# may need to overwrite the value
# very similar to LEETCODE 286

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def dfs(i, j, depth):
            if i <0 or j <0 or i>m-1 or j>n-1:
                return 
            elif rooms[i][j] > depth :
                rooms[i][j] = depth
                depth += 1
                dfs(i+1, j, depth)
                dfs(i, j+1, depth)
                dfs(i-1, j, depth)
                dfs(i, j-1, depth)
            else:
                return
        
        if not rooms:
            return rooms
        
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i+1, j, 1)
                    dfs(i, j+1, 1)
                    dfs(i-1, j, 1)
                    dfs(i, j-1, 1)
