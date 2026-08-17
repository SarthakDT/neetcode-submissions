class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = -1

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                m = i
                break

        if m == -1:
            return False

        l = 0
        r = len(matrix[0]) - 1

        # Binary search within the row
        while l <= r:
            mid = (l + r) // 2

            if matrix[m][mid] == target:
                return True

            elif matrix[m][mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False