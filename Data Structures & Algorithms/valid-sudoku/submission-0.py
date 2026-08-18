class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashset = [set() for _ in range(9)]
        col_hashset = [set() for _ in range(9)]
        square_hashset = [set() for _ in range(9)]

        for row_index,row in enumerate(board):
            for col_index, element in enumerate(row):
                if element == ".":
                    continue
                
                square_index = (row_index // 3) * 3 + (col_index // 3)

                if element in row_hashset[row_index]:
                    return False
                else:
                    row_hashset[row_index].add(element)

                if element in col_hashset[col_index]:
                    return False
                else:
                    col_hashset[col_index].add(element)

                if element in square_hashset[square_index]:
                    return False
                else:
                    square_hashset[square_index].add(element)

        return True

