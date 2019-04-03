class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = '({['
        result = list()
        for c in s:
            if c in open_brackets:
                result.append(c)
            else:
                if len(result) == 0:
                    return False
                if c == ')':
                    if result.pop() != '(':
                        return False
                if c == '}':
                    if result.pop() != '{':
                        return False
                if c == ']':
                    if result.pop() != '[':
                        return False
        if len(result) > 0:
            return False
        return True

            
