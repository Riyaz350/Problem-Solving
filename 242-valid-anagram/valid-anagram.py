class Solution(object):
    def isAnagram(self, s, t):
        if len(t)!=len(s):
            return False;
        dic1 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1;
            else:
                dic1[i] +=1;
                
        for i in t:
            if i in dic1 and dic1[i] != 0:
                dic1[i] -=1;
            else:
                return False;
        return True