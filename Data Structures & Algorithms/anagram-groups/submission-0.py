class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(s):
            if len(s) == 0:
                return "-1"
            ss = sorted(s)
            newS = ""
            cl = ss[0]
            cnt = 0
            for c in ss:
                if c == cl:
                    cnt = cnt + 1
                    continue
                newS = newS + cl + str(cnt)
                cnt = 1
                cl = c
            return newS + cl + str(cnt)
        anaDict = {}
        for s in strs:
            key = getKey(s)
            anaDict.setdefault(key, list()).append(s)
        return list(anaDict.values())
