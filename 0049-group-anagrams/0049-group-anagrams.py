from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for i in strs:
            s=sorted(i)
            x=''.join(s)
            if x not in m:
                m[x]=[i]
            else:
                m[x].append(i)
        return m.values()
        