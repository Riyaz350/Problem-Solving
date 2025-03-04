class Solution(object):
    def findContentChildren(self, g, s):
        g.sort(reverse = True)
        s.sort(reverse = True)
        res, i , j = 0,0, 0
        while i< len(g) and j<len(s):
            if g[i] <= s[j]:
                res+=1;
                j+=1;
                i+=1;
            else:
                i+=1;
        return res