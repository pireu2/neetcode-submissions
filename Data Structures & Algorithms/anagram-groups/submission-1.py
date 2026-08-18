class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            c_dict = {}

            for c in string:
                c_dict[c] = c_dict.get(c, 0), + 1

            key = frozenset(c_dict.items())
            if key not in result:
                result[key] = []
            result[key].append(string)

        return list(result.values())