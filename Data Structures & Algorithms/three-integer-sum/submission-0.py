class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = set()

        for i in range(len(sorted_nums)):
            target = -sorted_nums[i]
            left = 0
            right = len(sorted_nums) - 1

            while left < right:
                sum_nums = sorted_nums[left] + sorted_nums[right]
                if sum_nums == target and left != i and right != i:
                    triplet = sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    output.add(tuple(triplet))
                
                if sum_nums < target:
                    left += 1
                else:
                    right -= 1
        
        return list(output)