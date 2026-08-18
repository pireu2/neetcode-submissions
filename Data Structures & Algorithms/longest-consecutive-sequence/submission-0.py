class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        num_set = set(nums)

        for num in num_set:

            if num - 1 not in num_set:
                curr_len = 0
                curr_num = num

                while curr_num in num_set:
                    curr_len += 1
                    curr_num += 1

                output = max(output, curr_len)



        return output