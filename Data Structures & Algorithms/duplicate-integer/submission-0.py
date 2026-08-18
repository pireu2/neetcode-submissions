class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for n in nums:
            if n not in set_nums:
                set_nums.add(n)
            else:
                return True
        
        return False