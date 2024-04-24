class Solution:
    def canCompleteCircuit(self, g: List[int], c: List[int]) -> int:

        if sum(g)<sum(c):
            return -1
        c_gas=0
        s_index=0
        for i in range(len(g)):
            c_gas+=g[i]-c[i]
            if c_gas<0:
                c_gas=0
                s_index=i+1
        return s_index