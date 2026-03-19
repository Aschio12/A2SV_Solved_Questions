s=input()

stuck,dp=[],[0]*len(s)

for i in range(len(s)):
    if s[i]=="(":
        stuck.append(i)
    else:
        if stuck:
            start=stuck.pop()
            current_len=i-start+1
            if start>0:
                current_len+=dp[start-1]
            dp[i]=current_len

maxx,count=0,1

for i in range(len(dp)):
    if dp[i]>maxx:
        maxx=dp[i]
        count=1
    elif dp[i]==maxx and dp[i]>0:
        count+=1
print(*[maxx,count])