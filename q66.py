class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ## first stage, reverse the order, it will be easilier 
        # digits=digits[::-1]
        # add = 1
        # for i in range(len(digits)):
        #     if digits[i]+add < 10:
        #         digits[i]+=1
        #         add = 0
        #         return digits
        #     elif digits[i]+add == 10:
        #         digits[i] = 0
        #         add = 1
        # if add == 1:
        #     digits = digits+[1]
        # return digits[::-1]
 
        #
        carry = 1
        start = len(digits)-1
        for i in range(start,-1,-1):
            if digits[i]+carry < 10:
                digits[i]+=1
                carry = 0
                return digits
            elif digits[i]+carry == 10:
                digits[i] = 0
                carry = 1
        if carry == 1:
            digits = [1] + digits
        return digits
 



    ## notice:
    ## must remember to consider "carry"
