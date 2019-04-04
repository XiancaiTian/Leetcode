class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        result = '1'
        for i in range(1,n):
            result_temp = ''
            count = 0
            last_char = result[0]
            for j in range(len(result)):
                if result[j] == last_char:
                    count += 1
                else:
                    result_temp += str(count) + result[j-1]
                    last_char = result[j]
                    count = 1
            result_temp += str(count) + result[j]
            result = result_temp
            print(i, result)
        return result



        
