class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{string}💀' for string in strs)
            

    def decode(self, s: str) -> List[str]:
        return s.split('💀')[:-1]