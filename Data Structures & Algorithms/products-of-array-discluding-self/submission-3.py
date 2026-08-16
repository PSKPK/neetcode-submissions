class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = 0
        for x in nums:
            if x == 0:
                cnt = cnt + 1
        totalProduct = int(math.prod(x for x in nums if x!=0))
        if cnt == 0:
            return [int(totalProduct/x) for x in nums]
        if cnt == 1:
            res = []
            for x in nums:
                res.append(0 if x!=0 else totalProduct)
            return res
        return [0 * len(nums)]