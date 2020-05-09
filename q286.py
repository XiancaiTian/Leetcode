## DFS solution
class Solution:
    """
    start from every gate and update the distance to rooms
    if the new distance is closer than the previous, then overwrite
    """
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # Edge case
        if not rooms:
            return
        
        def dfs(i, j, depth):
            # hit the boundary
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols:
                return
            
            # hit the wall
            if rooms[i][j] == -1:
                return
            
            # pruning
            if rooms[i][j] < depth:
                return
                
            # update the distance
            rooms[i][j] = min(depth, rooms[i][j])
            depth += 1
            dfs(i+1, j, depth)
            dfs(i, j+1, depth)
            dfs(i-1, j, depth)
            dfs(i, j-1, depth)
            
        
        n_rows, n_cols = len(rooms), len(rooms[0])
        depth = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if rooms[i][j] == 0:
                    dfs(i, j, depth)



class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return
        
        h = len(rooms)
        w = len(rooms[0])
        
        # start with the gates
        q = []
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        # use bfs to fill out the whole matrix
        while q:
            # first come, first serve
            row, col = q.pop(0)
            # dist add one and assign to the next step
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                # keep growing and append the queue
                if 0 <= r < h and 0 <= c < w and rooms[r][c] == 2147483647:
                    rooms[r][c] = dist
                    q.append((r,c))
