class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        for i in accounts:
            if sum(i) > max:
                max = sum(i)
        return max

        