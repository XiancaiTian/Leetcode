class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            # use num to accumulate the number with digits >=1
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            # if encounter a new sigh
            if s[i] in "+-*/" or i == len(s) - 1:
                # comine the operation and number in to 'num'
                if sign == "+":
                    stack.append(num)
                # comine the operation and number in to '-num'
                elif sign == "-":
                    stack.append(-num)
                # extract the last number and multiply
                elif sign == "*":
                    stack.append(stack.pop()*num)
                # extract the last number and divide
                else:
                    stack.append(int(stack.pop()/num))
                # reset number
                num = 0
                # save the previous sign
                sign = s[i]
                
        return sum(stack)
