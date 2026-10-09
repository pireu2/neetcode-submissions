class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        water_sum = 0

        left = 0
        right = len(height) - 1

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            water_sum += min(max_left, max_right) - ( height[left]  if height[left] < height[right] else height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water_sum