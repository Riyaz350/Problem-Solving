class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag= {}
        ans = True;
        for i, num in enumerate(magazine):
            if num in mag:
                mag[num] +=1;
            else:
                mag[num] = 1;
        
        for i in ransomNote:
            if i in mag and mag[i] != 0:
                mag[i]-=1 ;
            else:
                ans = False;
        return ans;