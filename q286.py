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
