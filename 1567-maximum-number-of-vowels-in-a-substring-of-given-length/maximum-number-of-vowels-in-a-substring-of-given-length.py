class Solution(object):
    def maxVowels(self, s, k):
        vow = set(['a', 'e', 'i', 'o', 'u'])
        l,count, ans = 0,0,0
        for i in range(len(s)):
            if i-l+1>k:
                count-=1 if s[l] in vow else 0
                l+=1
            if s[i] in vow:
                count +=1
            ans = max(ans, count)
        return ans