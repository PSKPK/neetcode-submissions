class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = 0
        for x in nums:
            if x == 0:
                cnt = cnt+1
        if cnt==len(nums):
            return nums
        has0 = True if 0 in nums else False
        totalProduct = math.prod( x for x in nums if x != 0 )
        finalRes = []
        if has0:
            for x in nums:
                finalRes.append( 0 if x != 0 else totalProduct)
        else:
            for x in nums:
                finalRes.append( totalProduct/x )
        return list(map(lambda x:int(x), finalRes))