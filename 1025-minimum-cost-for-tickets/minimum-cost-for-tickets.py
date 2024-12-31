class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        mem = {}

        def rec(day):
            if day > days[-1]:
                return 0
            if day not in days:
                return rec(day+1)
            if day in mem:
                return mem[day]
            
            mem[day] = min(
                costs[0] + rec(day+1),
                costs[1] + rec(day+7),
                costs[2] + rec(day+30)
            )

            return mem[day]
            

        return rec(1)