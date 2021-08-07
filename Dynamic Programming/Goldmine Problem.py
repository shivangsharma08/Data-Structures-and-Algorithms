n=int(input())
m=int(input())
arr=[]
for i in range(0,n):
    arr.append([int(j) for j in input().strip().split()])
dp=[[0]*m for i in range(n)]
out=[]
for j in range(m-1,-1,-1):
    for i in range(n-1,-1,-1):
        if(j==m-1):
            dp[i][j]=arr[i][j]
        elif(i==0):
            dp[i][j]=max(dp[i][j+1],dp[i+1][j+1])+arr[i][j]
        elif(i==n-1):
            dp[i][j]=max(dp[i-1][j+1],dp[i][j+1])+arr[i][j]
        else:
            dp[i][j]=max(dp[i-1][j+1],dp[i][j+1],dp[i+1][j+1])+arr[i][j]
for i in range(len(dp)):
    out.append(dp[i][0])
print(max(out))