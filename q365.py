class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # make x larger
        if x < y:
            x, y = y, x
        
        # weired case, zero is measurable
        if not z:
            return True
        
        elif (z > x+y) or not y:
            return False
        
        # Euclidean algorithm
        while y:
            r = x%y
            x = y
            y = r
            
        # x is the previous y
        return not z%x 
