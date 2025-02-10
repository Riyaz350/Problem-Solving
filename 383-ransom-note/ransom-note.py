class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = "".join(sorted(ransomNote))
        magazine = "".join(sorted(magazine))
        i=0;
        j=0;
        while i <= len(ransomNote)-1 and j< len(magazine):
            while j<=len(magazine)-1:
                if ransomNote[i] == magazine[j]:
                    i+=1;
                    j+=1;
                    break;
                else:
                    j+=1;
        return i == len(ransomNote)