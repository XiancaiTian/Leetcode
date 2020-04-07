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

                    
## LEETCODE 130
# concept: start from edges and mark the suitable positions
# replace the marked positions by 'O'
# label the rest as 'X'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or board[i][j]=='X' or board[i][j]=='Y' :
                return
            # 'Y' is a placeholder
            board[i][j] = 'Y' 
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or j ==0 or i == m-1 or j ==n-1) :
                    dfs(i,j)

        # replace O by X, Y by O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'

                    
                    
## LEETCODE 339
# concept: dfs
# need to notice the .getInteger() and .getList()
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        self.ans = 0
        depth = 1
        for ele in nestedList:
            self.dfs(ele, depth)
        return self.ans
    
    def dfs(self, ele, depth):
        if ele.getInteger():
            self.ans += ele.getInteger()*depth
            return
        for ele_lower in ele.getList():
            self.dfs(ele_lower, depth+1)
