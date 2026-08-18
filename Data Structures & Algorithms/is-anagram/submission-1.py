class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for c in s:
            if c not in hash_s:
                hash_s[c] = 1
            else:
                hash_s[c] += 1
        
        for c in t:
            if c not in hash_t:
                hash_t[c] = 1
            else:
                hash_t[c] += 1

        if len(hash_s.keys()) != len(hash_t.keys()):
            return False

        for key_s,value_s in hash_s.items():
            if key_s not in hash_t:
                return False

            if hash_t[key_s] != value_s:
                return False

        return True