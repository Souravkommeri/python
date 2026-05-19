def stair(n):
    if n<=2:
        return n
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[i]


#m=stair(5)
#print(m)
m=int(input("Enter the number"))
print(stair(m))
