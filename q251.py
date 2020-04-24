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
