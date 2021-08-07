import math
n=int(input())
arr=[]
dp=[None]*(n+1)
dp[n]=0
for _ in range(n):
    arr.append(int(input()))
for i in range(n-1,-1,-1):
    if(arr[i]>0):
        mn = math.inf
        for j in range(1,arr[i]+1):
            if(i+j<len(dp)):
                if(dp[i+j]!=None):
                    mn=min(mn,dp[i+j])
        if(mn!=math.inf):
            dp[i]=mn+1
print(dp[0])