a,p=input().split()
a=int(a)
p=int(p)
balu=''
rt=2
if(a+p<=3):
    for i in range(0,a+p):
        if(i%2!=0):
            balu=balu+'0'
        else:
            balu=balu+'1'
else:    
    for i in range(0,a+p):
        if(i==rt):
            balu=balu+'0'
            if(rt==p):
                rt=rt+2
            else:
                rt=rt+3
        else:
            balu=balu+'1'
x=len(balu)-1
if(int(balu[x])==0):
    print('-1') 
elif a==1 and p==2: 
     print("011")
else:
    print(balu)
