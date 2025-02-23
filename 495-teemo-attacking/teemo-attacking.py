class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = 0;
        for i in range(1,len(timeSeries)):
            if duration < timeSeries[i] - timeSeries[i-1]:
                ans+=duration;
            else:
                ans += (timeSeries[i] - timeSeries[i-1])
        ans+=duration
        return ans