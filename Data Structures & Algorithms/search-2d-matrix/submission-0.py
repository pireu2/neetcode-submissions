class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(nums: List[int], target):

            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return True
            
            return False

        first_col = [x[0] for x in matrix]

        left, right = 0, len(first_col) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True


        return search(matrix[right], target)

        