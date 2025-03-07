class Solution(object):
    def maxOperations(self, nums, k):
        c = Counter(nums)
        seen = set()
        count =0
        for i in nums:
            if i == k-i and i not in seen:
                if c[i]>1:
                    seen.add(i)
                    count += c[i]//2
                else:
                    continue
            if k-i in c and i not in seen and k-i not in seen:
                count += min(c[i], c[k-i])
                seen.add(i)
                seen.add(k-i)
        return count

