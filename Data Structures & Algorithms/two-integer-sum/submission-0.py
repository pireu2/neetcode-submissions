class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_t = {}

        for index, num in enumerate(nums):
            if num in hash_t:
                return [nums.index(hash_t[num]), index]
            else:
                hash_t[target - num] = num
