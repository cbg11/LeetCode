class Solution(object):
    def findTheDifference(self, s, t):
        temp = []
        for i in t:
            if s.count(i) != t.count(i):
                return i