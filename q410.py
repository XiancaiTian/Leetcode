class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canDivide(nums, mid, n_split):
            """
            因為要用binary search來解，
            於是仿照isBadVersion function，我們建立了canDivide function...

            如果以mid為cut-off切出來的array塊數超過n_split, 就不可以
            以[7,2,5,10,8]為例，以mid = 12來切，會變成 [7,2], [5], [10], [8] , 有四塊
            ===================================================================
            每當前面的和大於mid, 就代表進入下一個split, 所以 count +=1
            如果count > n_split 代表爆了，mid不夠大，才會切成這麼多塊 ==> return False  
            如果用完了nums所有element 都沒有爆 ==> return True
            """
            total, count = 0, 1
            for n in nums:
                if total+n <= mid:
                    total += n
                else:
                    total = n
                    count += 1
                if count > n_split:
                    return False
            return True
        
        
        """
        依據題意，我們想要minimize the largest sum
        我們可以套用binary search的lower bound模板
        已經知道答案會落在 這個array的最大值 和這個array的sum之間
        """
        l , r  = max(nums), sum(nums)
        
        #for i in range(l,r):
        #    print(i, canDivide(nums, i, m))
        
        while l <= r:
            mid = l + (r-l)//2
            if canDivide(nums, mid, m):
                r = mid  - 1
            else:
                l = mid + 1
        return l
    

