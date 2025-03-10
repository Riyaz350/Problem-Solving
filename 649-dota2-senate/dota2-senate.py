class Solution(object):
    def predictPartyVictory(self, senate):
        r_queue = deque([i for i, s in enumerate(senate) if s=="R"])
        d_queue = deque([i for i, s in enumerate(senate) if s =="D"])
        next_pos = len(senate)
        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:
                r_queue.append(next_pos)
            else:
                d_queue.append(next_pos)
            r_queue.popleft()
            d_queue.popleft()
            next_pos +=1
        return "Radiant" if r_queue else "Dire"