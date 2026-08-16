class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([chr(300)+s for s in strs])

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        if s[0]==chr(300):
            s = s[1:]
        return s.split(chr(300))