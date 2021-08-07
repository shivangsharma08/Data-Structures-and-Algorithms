n=int(input())
arr=[]
dp=[0]*(n+1)
dp[n]=1
for _ in range(n):
    arr.append(int(input()))
for i in range(n-1,-1,-1):
    for j in range(1,arr[i]+1):
        if(i+j<len(dp)):
            dp[i]+=dp[i+j]
        else:
            break
print(dp[0])