class Solution(object):
    def swimInWater(self, grid):
        N = len(grid)

        def possible(T):
            stack = [(0, 0)]
            seen = {(0, 0)}
            while stack:
                r, c = stack.pop()
                if r == c == N-1: return True
                for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if (0 <= cr < N and 0 <= cc < N
                            and (cr, cc) not in seen and grid[cr][cc] <= T):
                        stack.append((cr, cc))
                        seen.add((cr, cc))
            return False

        l, r = grid[0][0], N * N
        while l < r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l
