class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        desc_list = [k for k, _ in sorted(num_dict.items(), key=lambda item: item[1], reverse=True)]
        return desc_list[:k]