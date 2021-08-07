n=int(input())
arr=[0]*n
for i in range(n):
    arr[i]=int(input())
tar=int(input())
dp=[[0]*(tar+1) for i in range(n+1)]
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if(i==0 and j==0):
            dp[i][j]=True
        elif(i==0):
            dp[i][j]=False
        elif(j==0):
            dp[i][j]=True
        else:
            if(dp[i-1][j]==True):
                dp[i][j]=True
            else:
                val=arr[i-1]
                if(j>=val):
                    if(dp[i-1][j-val]==True):
                        dp[i][j]=True
print(dp[len(arr)][tar])