# time complexity: o(n)
# space complexity: 0(1)
# ran on leetcode: yes


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height = len(matrix)
        width = len(matrix[0])

        # start pointer in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False
