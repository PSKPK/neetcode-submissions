class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        for s in strs:
            key = ''.join(sorted(s))
            anaDict.setdefault(key, []).append(s)
        return list(anaDict.values())
