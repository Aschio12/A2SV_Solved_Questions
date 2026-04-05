def rec(idx,current):
    global ans
    if idx==n:
        tot=sum(current)
        if tot>=l and tot<=r:
            if max(current)-min(current)>=x:
                ans+=1
        return

    current.append(arr[idx])
    rec(idx+1,current)
    current.pop()
    rec(idx+1,current)

    
    
   



rec(0,[])
print(ans)