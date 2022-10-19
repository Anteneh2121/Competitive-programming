# iven a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two  same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxFreq = 0
        max_count = 0
        dic = {}
        for task in tasks:
            if task in dic:
                dic[task] += 1
            else:
                dic[task] = 1
            if dic[task] > maxFreq:
                maxFreq = dic[task]
                max_count = 1
            elif dic[task] == maxFreq:
                max_count += 1
        
        if len(dic) <= n+1:
            return (maxFreq-1) * (n+1) + max_count
        else:
            return max((maxFreq-1) * (n+1) + max_count, len(tasks))
        
