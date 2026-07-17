class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search O(log mn)

        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW -1

        while top <= bot:
            m_row = (top+bot)//2
            if target > matrix[m_row][COL-1]:
                top = m_row +1
            elif target < matrix[m_row][0]:
                bot = m_row - 1
            else: 
                break

        if top > bot:
            return False

        m_row = (top + bot) //2

        l, r = 0, COL-1

        while l<=r:
            m_col = (l+r)//2
            if target > matrix[m_row][m_col]:
                l = m_col +1
            elif target < matrix[m_row][m_col]:
                r = m_col -1
            else: 
                return True
        return False                                    


    
        
        