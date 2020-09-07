# https://leetcode.com/problems/zigzag-iterator/discuss/71786/Python-O(1)-space-solutions
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.n = 0
        self.max = len(v1)+len(v2)
        def helper():
            for i in itertools.count():
                for v in [self.v1, self.v2]:
                    if i < len(v):
                        yield v[i]
                    
        self.val = helper() 

    def next(self) -> int:
        self.n +=1
        return next(self.val)
    
    def hasNext(self) -> bool:
        return self.n < self.max
 
        
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
