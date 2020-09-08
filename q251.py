class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        def get():
            for arr in vec2d:
                for item in arr:
                    yield item
        self.own_iter = iter(get())
        self.latest = next(self.own_iter, None)
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            t = self.latest
            self.latest = next(self.own_iter, None)
            return t
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.latest != None

    
   # ==================

class Vector2D:

    def __init__(self, v: List[List[int]]):
        
        def val():
            for inner in v:
                for element in inner:
                    yield element
            
        self.val = val()
        self.peek = None

    def next(self) -> int:
        if self.hasNext():
            ans = self.peek
            self.peek = None
            return ans

    def hasNext(self) -> bool:
        if self.peek is not None:
            return True
        try:
            self.peek = next(self.val)
            return True
        except:
            return False
