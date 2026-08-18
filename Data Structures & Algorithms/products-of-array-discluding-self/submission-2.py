class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size

        left = 1
        for i in range(size):
            result[i] *= left
            left*= nums[i]

        right = 1
        for i in range(size)[::-1]:
            result[i] *= right
            right*= nums[i]

        return result