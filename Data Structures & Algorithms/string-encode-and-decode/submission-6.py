class Solution:

    def encode(self, strs: List[str]) -> str:
        return chr(300).join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(chr(300))
