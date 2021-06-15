t=int(input())
while(t):
    n=int(input())
    ar=[int(i) for i in input().strip().split()]
    s=[]
    top=-1
    out=[]
    for i in range(n):
        if (len(s) == 0):
            out.append(-1)
        elif (len(s) > 0 and s[top] < ar[i]):
            out.append(s[top])
        elif (len(s) > 0 and s[top] >= ar[i]):
            while (len(s) > 0 and s[top] >= ar[i]):
                s.pop()
                top-=1
            if (len(s) == 0):
                out.append(-1)
            else:
                out.append(s[top])
        s.append(ar[i])
        top+=1
    print(*out)
    t=t-1