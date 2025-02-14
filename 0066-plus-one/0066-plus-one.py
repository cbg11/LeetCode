class Solution(object):
    def plusOne(self, digits):
        n = int("".join(map(str, digits)))
        n = n + 1
        digits = list(map(int, str(n)))
        return digits
        