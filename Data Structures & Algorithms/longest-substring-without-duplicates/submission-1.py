class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        max_dif = 0
        start = 0
        end = 0

        while end < len(s):
            if s[end] in seen:
                while s[end] in seen:
                    seen.remove(s[start])
                    start += 1   
            
            seen.add(s[end])
            max_dif = max(max_dif, end - start + 1)
            end += 1


        
        return max_dif