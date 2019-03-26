class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if '.' in version1:
            v1 = version1.split('.')
        else:
            v1 = [version1]
        
        if '.' in version2:
            v2 = version2.split('.')
        else:
            v2 = [version2]
        
        diff = len(v2)-len(v1)
        if diff>0:
            v1 = v1+[0]*diff
        elif diff<0:
            diff*=(-1)
            v2 = v2+[0]*diff
        for i, value in enumerate(v1):
            compare = int(value) - int(v2[i])
            if compare > 0:
                return 1
            elif compare < 0:
                return -1
        return 0
            
