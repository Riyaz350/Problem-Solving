class Solution(object):
    def isAnagram(self, s, t):
        dic1={}
        dic2={}
        if len(s) != len(t):
            return False;
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = 1
            else:
                dic1[s[i]] += 1;
            if t[i] not in dic2:
                dic2[t[i]] = 1
            else:
                dic2[t[i]] += 1;
        for i in s:
            if i not in dic2:
                return False;
            if dic1[i] != dic2[i]:
                return False;
        return True