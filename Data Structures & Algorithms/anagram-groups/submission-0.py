class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            freq = [0]*26
            for c in string:
                freq[ord(c) - ord('a')] += 1

            freq_str = str(freq)
            if freq_str not in result:
                result[freq_str] = [string]
            else:
                result[freq_str].append(string)

        return list(result.values())