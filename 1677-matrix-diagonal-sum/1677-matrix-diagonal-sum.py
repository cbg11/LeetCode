class Solution(object):
    def diagonalSum(self, mat):
        values = []
        indexes = []
        for i, n in enumerate(mat):
            for j, m in enumerate(n):
                if i == j:
                    values.append(m)
                    indexes.append([i,j])
            if [i,(len(n) - 1) - i] not in indexes:
                values.append(n[(len(n) - 1) - i])
        return sum(values)
        