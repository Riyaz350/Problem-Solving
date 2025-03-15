class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        max_val = max(candies)
        for i in candies:
            if i + extraCandies >= max_val:
                ans.append(True)
            else:
                ans.append(False)

        return ans