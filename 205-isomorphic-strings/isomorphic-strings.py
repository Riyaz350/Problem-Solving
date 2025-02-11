class Solution(object):
    def isIsomorphic(self, s, t):
        dict1 = {}
        ans= ''
        testString =''
        for i in range(len(s)):
            if s[i] in dict1:
                continue;
            elif t[i] not in testString:
                dict1[s[i]]= t[i]
                testString += t[i]
            else:
                dict1[s[i]]= ''
            
        for i, l in enumerate(s):
            ans =ans+ dict1[l]
        return ans == t