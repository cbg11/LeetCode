class Solution(object):
    def setZeroes(self, matrix):
        indexes = []
        for i, m in enumerate(matrix):
            for j, n in enumerate(m):
                if n == 0:
                    indexes.append([i,j])
        for i in indexes:
            for j in range(len(matrix[0])):
                matrix[i[0]][j] = 0
            for j in range(len(matrix)):
                matrix[j][i[1]] = 0
        