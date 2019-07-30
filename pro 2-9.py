as=int(input())
p=[]
x=""
for i in range(as):
	l1=list(map(int,input().split()))
	for j in l1:
		p.append(j)
p.sort()
for i in l:
	x=x+str(i)+" "
print(x.strip())
