class Solution(object):
    def getModifiedArray(self, length, updates):
        # store the operation information in res
        res = [0] * length
        for start, end, update in updates:
            res[start] += update
            
            # if not last position
            if end != length -1:
                res[end+1] -= update
        
        # rolling sum
        # if not stated, the value for the current point is same as the previous
        for i in range(1,length):
             res[i] += res[i-1]

        return (res)
