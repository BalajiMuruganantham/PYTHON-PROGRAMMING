from itertools import combinations
ab,x=map(int,input().split())
l=len(str(ab))
c=list(combinations(str(ab),l-x))
c=sorted(c)
print(*c[0],sep='')
