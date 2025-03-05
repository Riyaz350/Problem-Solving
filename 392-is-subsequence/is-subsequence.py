class Solution(object):
    def isSubsequence(self, s, t):
        s= list(s)
        t= list(t)
        k=0
        j=0
        if s and t:
            while j< len(t) and k<len(s):
                if t[j] != s[k]:
                    j+=1
                else:
                    k+=1
                    j+=1
        elif len(s)==0:
            return True

        return k == len(s)
                    