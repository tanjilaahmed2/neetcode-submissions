class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bruteforce O(m*n)
        ROW = len(matrix)
        COL = len(matrix[0])


        for m in range(ROW):
            for n in range(len(matrix[m])):
                if target == matrix[m][n]:
                    return True
        return False            

        