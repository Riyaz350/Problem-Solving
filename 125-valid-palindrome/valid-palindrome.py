class Solution(object):
    def isPalindrome(self, s):
        s= "".join(c.lower() for c in s if c.isalnum())
        new = ''
        for i in range(len(s)-1, -1, -1):
            new+=s[i]
        
        return s==new