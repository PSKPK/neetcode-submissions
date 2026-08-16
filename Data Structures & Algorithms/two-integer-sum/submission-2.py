class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sN = sorted(nums)
        ri = len(nums)-1
        li = 0
        while li < ri:
            if sN[li] + sN[ri] == target:
                break
            if sN[li] + sN[ri] > target:
                ri = ri-1
            if sN[li] + sN[ri] < target:
                li = li + 1
        v1=sN[li]
        v2=sN[ri]
        s1 = None
        s2 = None
        for a in range(0, len(nums)):
            if nums[a]==v1:
                s1 = a
                break
        for a in range(0, len(nums)):
            if a == s1:
                continue
            if nums[a]==v2:
                s2 = a
                break
        return [min(s1,s2), max(s1,s2)]
