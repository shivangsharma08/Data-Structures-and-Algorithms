while(t):
    n=int(input())
    ar=[int(i) for i in input().strip().split()]
    stack=[]
    ans=[]
    difference=0
    i=0
    while i<len(ar):
        while len(stack)>0 and stack[-1][1]<=ar[i]:
            stack.pop()
        if len(stack)>0:
            difference=i-stack[-1][0]
            ans.append(difference)
        else:
            ans.append(i+1)
        stack.append((i,ar[i]))
        i+=1
    print(*ans)
    t=t-1