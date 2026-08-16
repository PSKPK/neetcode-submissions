class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return None
        wholeStr = ""
        for s in strs:
            ordS = ""
            for c in s:
                ordS = f'{ordS}@{ord(c)}'
            wholeStr = f'{wholeStr},{ordS}'
        return wholeStr

    def decode(self, s: str) -> List[str]:
        if s == None:
            return []
        if len(s)==0:
            return [s]
        if s[0]== ',':
            s = s[1:]
        words = s.split(',')
        return list(map(lambda x: ''.join(list(map(lambda y: chr(int(y)) if y!='' else '', x.split('@')))), words))