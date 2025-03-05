class Solution(object):
    def maxOperations(self, nums, k):
        c = Counter(nums)
        count = 0
        seen = set()

        for i in c:
            if k-i in c and i not in seen:
                if k-i == i:
                    count+= c[i]//2
                else:
                    count+= min(c[i], c[k-i])
                seen.add(i)
                seen.add(k-i)
        return count
