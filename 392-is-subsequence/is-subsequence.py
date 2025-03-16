class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s= list(s)
        t= list(t)
        i = 0
        for j in range(len(t)):
            if not s:
                return True
            if i<len(s) and s[i] == t[j]:
                i+=1
            else:
                continue
        return i == len(s)