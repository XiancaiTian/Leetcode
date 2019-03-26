class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # extract the sign
        sign = 0
        dividend = self.checkinput(dividend)
        divisor = self.checkinput(divisor)
        dividend, divisor = str(dividend), str(divisor)
        if dividend[0]=='-':
            sign = sign+1
            dividend = dividend[1:]
        if divisor[0]=='-':
            sign = sign-1
            divisor = divisor[1:]
        if sign!= 0:
            sign = '-'
        else:
            sign = '0'
            
        ###
        digits = len(divisor)
        divisor = int(divisor)
        q, r = self.div(int(dividend[:digits]), divisor)
        ans = [str(q)]
        while digits <= len(dividend)-1:
            q, r = self.div(int(dividend[digits])+10*r, divisor)
            ans.append(str(q))
            digits += 1
        ans = int(''.join([sign]+ans))
        return self.checkinput(ans)
            
    def div(self, dividend, divisor):
            # must be positive and less than 10 times differences...
            start = 0
            if dividend == 0:
                return 0, 0
            for i in xrange(1, 11, 1):
                start += divisor
                if start > dividend:
                    q = i-1
                    r = dividend - (start - divisor)
                    return q, r
                
    def checkinput(self, ans):
        if ans < -2147483648:
            return -2147483648
        elif ans > 2147483647:
            return 2147483647
        else:
            return ans
                
