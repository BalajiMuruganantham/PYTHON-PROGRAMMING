def re(bal,sz):
    res=[]
    count=1
    for i in range(0,sz-1):
        if bal[i]<bal[i+1]:
            count+=1
        else:
            res.append(count)
            count=1
    res.append(count)
    print(max(res))
sz=int(input())
bal=list(map(int,input().split()))
re(bal,sz)
