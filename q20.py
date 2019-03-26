class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {"(":")","{":"}","[":"]"}
        bag = []
        q, r = divmod(len(s),2)
        if r!=0:
            return False
        
        for char in s:
            # case 1: get rostral parentheses
            if char in parentheses.values():
                if not bag:
                    return False
                # can only remove the last element in bag
                elif char == bag[-1]:
                    bag = bag[:-1]
                else:
                    return False
            # case 2: get caudal parentheses
            else:
                bag.append(parentheses[char])
        if bag: return False
        else: return True
