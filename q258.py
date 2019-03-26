class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        36 --> 9
        37 --> 10 -->1
        38 --> 11-->2
        39 --> 12-->3
        40 --> 4
        41 --> 5
        ...
        45 ---> 9
        46 --> 10 --> 1
        47 --> 11--> 2
        
        108 ---> 9
        
        '''
        q, r = divmod(num, 9)
        if r == 0 and q!=0:
            return 9
        else:
            return r
