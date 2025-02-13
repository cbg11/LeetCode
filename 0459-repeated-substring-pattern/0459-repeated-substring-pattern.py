class Solution(object):
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
        d_s = s + s
        m_d_s = d_s[1:-1]
        return s in m_d_s
        