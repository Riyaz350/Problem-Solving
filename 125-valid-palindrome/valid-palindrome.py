class Solution(object):
    def isPalindrome(self, s):
        s=  ''.join(c.lower() for c in s if c.isalnum())
        ans = True;
        first = 0
        last = len(s) - 1
        for i in range(int(len(s)/2)):
            if s[first] == s[last]:
                first = first +1;
                last  = last - 1;
            else:
                ans = False;
        return ans