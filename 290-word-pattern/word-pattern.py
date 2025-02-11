class Solution(object):
    def wordPattern(self, pattern, s):
        dic1  = {}
        dic2 =  {}
        s = s.split()
        for i in range(len(s)):
            if len(s) != len(pattern):
                return False;
            if  pattern[i] not in dic1:
                dic1[pattern[i]] = i
            if s[i] not in dic2:
                dic2[s[i]] = i
            
            if dic1[pattern[i]] != dic2[s[i]]:
                return False;
        return True;