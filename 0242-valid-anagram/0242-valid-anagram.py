class Solution(object):
    def isAnagram(self, s, t):
        temp = True
        if len(s) != len(t):
            return False
        for i in t:
            if s.count(i) != t.count(i):
                temp = False
                break
        return temp

        