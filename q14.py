class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        common = test = ''
        for w in strs[0]:
            test += w
            # two negative == positive trick...
            # if list empty, means test is in every str
            n = len(test)
            if not [test for s in strs[1:] if test!=s[:n]]:
                common = self.maxstr(common, test)
        return common
            
    def maxstr(self, str1, str2):
        if len(str2)>len(str1):
            return str2
        else:
            return str1
        
    ## Note: this is asking about "prefix", not all kinds of common strings
        
