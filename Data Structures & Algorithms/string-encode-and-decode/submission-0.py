class Solution:

    def encode(self, strs: List[str]) -> str:
        wholeStr = ""
        for s in strs:
            ordS = ""
            for c in s:
                ordS = f'{ordS}@{ord(c)}'
            wholeStr = f'{wholeStr},{ordS}'
        return wholeStr

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return [s]
        if s[0]== ',':
            s = s[1:]
        words = s.split(',')
        return list(map(lambda x: ''.join(list(map(lambda y: chr(int(y)) if y!='' else '', x.split('@')))), words))