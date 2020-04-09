# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Concept: see the comma or reach the end => send the thing to the recursion function

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[':
            return NestedInteger(int(s))
        nested = NestedInteger()
        # numP: whether the square brackets reach to the end
        numP = 0
        # index of the start
        start = 1
        for i in range(1, len(s)):
            if (numP == 0 and s[i] == ',') or i == len(s) - 1:
                # make sure it is not an empty string
                if start < i:
                    print(s[start:i])
                    nested.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == '[':
                numP += 1
            elif s[i] == ']':
                numP -= 1
        return nested
