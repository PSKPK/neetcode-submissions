class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for entry in nums:
            freq[entry] = freq.get(entry,0)+1
        orderByFreq = sorted(freq.keys(), key=lambda x:freq[x])
        return orderByFreq[-k:]