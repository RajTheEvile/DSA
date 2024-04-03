class Solution:
    def calPoints(self, x: List[str]) -> int:
        s=[]
        for i in x:
            if i=='+':
                x=s[-1]
                y=s[-2]
                s.append(x+y)
            elif i=="D":
                x=s[-1]
                s.append(x*2)
            elif i=="C":
                s.pop()
            else:
                s.append(int(i))
            #print(s)
        return sum(s)
        