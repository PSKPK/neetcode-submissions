class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newLis = sorted(nums)
        for n in range(0, len(newLis)-1):
            if newLis[n] == newLis[n+1]:
                return True
        return False