class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        i = 0
        container = [0]*len(strs)
        while True:
            for idx,val in enumerate(strs):
                if i == len(val):
                    return result
                else:
                    container[idx] = val[i]
            if len(set(container)) == 1:
                result += container[0]
            else:
                return result
            i += 1
