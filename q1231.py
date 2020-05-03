class Solution:
    """
    very similar to leetcode 410
    1, need to change line 12 from total = n to total = n
    2, need to change make n_splits equal to K+ 1, not K\
    3, need to start from min(sweetness) , in line 30
    """ 
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def canCut(sweetness, mid, n_splits= K+1):
            total, count = 0, 1
            """
            # leetcode 410 的目標是每一塊都不要比mid大
            mid = 9, [5,6,7,8,9,1,2,3,4] ---> [[5], [6], [7], [8], [9], [1,2,3],[4]]
            
            # leetcode 1231 的目標是每一塊都要比mid大
            mid = 9, [5,6,7,8,9,1,2,3,4] ---> [[5,6], [7,8], [9], [1,2,3,4]]
            """
            for n in sweetness:
                if total + n <= mid:
                    total +=n 
                else:
                    count +=1
                    total = 0 # 就是這裡要改!!!
                if count > n_splits:
                    return False
            return True
        """
        # for debugging purpose
        l , r = 0, sum(sweetness)
        for i in range(l , r ):
            print(i, canCut(sweetness, i))
        """
        
        """
        binary search會return sweetness cut-off
        只要sweetness大於等於cut-off, 就可以被稱做為一塊蛋糕  
        要注意，搜索範圍會是由 min(sweetness)開始、而不是由 max(sweetness)開始
        """
        l , r = min(sweetness), sum(sweetness)
        while l < r:
            mid = l + (r-l) //2
            if canCut(sweetness, mid):
                r = mid
            else:
                l = mid + 1
        return l
        
        
    
