class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = set()

        for i in range(len(sorted_nums)):
            target = -sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                sum_nums = sorted_nums[left] + sorted_nums[right]
                if sum_nums == target and left != i and right != i:
                    output.add((sorted_nums[i], sorted_nums[left], sorted_nums[right]))
                
                if sum_nums < target:
                    left += 1
                else:
                    right -= 1
        
        return list(output)