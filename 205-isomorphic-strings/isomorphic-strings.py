class Solution(object):
    def isIsomorphic(self, s, t):
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = i
            if t[i] not in dict2:
                dict2[t[i]] = i
            
            if dict1[s[i]] != dict2[t[i]]:
                return False;
        return True;