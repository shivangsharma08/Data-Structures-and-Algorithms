t=int(input())
while(t):
    s=input()
    inp=list(s)
    top=-1
    f=0
    ar=[]
    for i in range(len(inp)):
        if (inp[i] == "{" or inp[i] == "(" or inp[i] == "["):
            ar.append(inp[i])
            top+=1
        elif(inp[i] == ")" and top!=-1):
            if(ar[top] == "("):
                ar.pop()
                top-=1
            else:
                f=1
                break
        elif(inp[i] == "}" and top!=-1):
            if(ar[top] == "{"):
                ar.pop()
                top-=1
            else:
                f=1
                break
        elif(inp[i] == "]" and top!=-1):
            if(ar[top] == "["):
                ar.pop()
                top-=1
            else:
                f=1
                break
        else:
            f=1
    if(len(ar)==0 and f==0):
        print("balanced")
    else:
        print("not balanced")
    t=t-1