class Solution:
    def leastInterval(self, x: List[str], interval: int) -> int:
        d=Counter(x)
        max_freq=max(d.values())
        m_freq_tasks=0
        for i in d:
            if d[i]==max_freq:
                m_freq_tasks+=1
        z=(max_freq-1)*(interval+1)+(m_freq_tasks)

        return max(z,len(x))
