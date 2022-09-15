class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=[1]*(len(matrix))
        cols=[1]*(len(matrix[0]))
        for i in range(len(rows)):
            for j in range(len(cols)):
                if matrix[i][j]==0:
                    rows[i]=0
                    cols[j]=0
        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i]==0 or cols[j]==0:
                    matrix[i][j]=0
        '''
        R=len(matrix)
        C=len(matrix[0])
        flag=1
        for i in range(0,R):
            if matrix[i][0]==0:
                flag=0
            for j in range(1,C):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(R-1,1,-1):
            for j in range(C-1,1,-1):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
            if flag==0:
                matrix[i][0]=0
        '''
        
        