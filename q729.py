class MyCalendar:

    def __init__(self):
        # 準備一個list of [list], 按照順序儲存slots
        # intvs = [[start1, end1],[start2, end3],..... ]
        self.intvs = []

    def book(self, start: int, end: int) -> bool:
        proposed_index = self.lowerBound(start)
        # 看看前一個slot的end是多少
        if proposed_index>0 and self.intvs[proposed_index-1][1]>start:
            return False
        # 看看下一個slot的start是多少
        if proposed_index<len(self.intvs) and self.intvs[proposed_index][0]<end:
            return False
        self.intvs.insert(proposed_index, [start, end])
        return True
        
    def lowerBound(self, target):
        # 修改自花花的左閉右開模板
        # 找到target 在已知的start之內的index
        # 如果start分布為[1,2,4,6,8]
        #  當target為4, 則return 2
        #  當target為5, 則return 3
        l, r = 0, len(self.intvs)
        while l < r:
            mid = l + (r-l)//2
            if self.intvs[mid][0] >=target:
                r = mid
            else:
                l = mid + 1
        return l
