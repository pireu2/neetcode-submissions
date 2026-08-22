class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        size = 0 
        count = {}

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            curr_size = right - left + 1

            if curr_size - max(count.values()) <= k:
                size = max(size, curr_size)
            else:
                count[s[left]] -= 1
                left += 1
            
            right += 1


        return size