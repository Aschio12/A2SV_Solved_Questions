def back(idx,current):
    global possible
    if idx==len(s2):
        possible+=1
        if current==target:
            return 1
        else:
            return 0
        
    if s2[idx]=="+":
        return 0+back(idx+1,current+1)

    elif s2[idx]=="-":
        return 0+back(idx+1,current-1)
    else:
        left=0+back(idx+1,current+1)
        right=0+back(idx+1,current-1)
        return left+right
    

t=back(0,0)
print(f"{t/possible:.12f}")