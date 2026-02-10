class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents={}
        for dirr in paths:
            current=dirr.split()
            root=current[0]
            for i in range(1,len(current)):
                current_file=current[i]
                cnt=""
                ff=""
                c=False
                for j in range(len(current_file)):
                    if current_file[j]=="(":
                        c=True
                    elif current_file[j]==")":
                        c=False
                    else:
                        if c:
                            cnt+=current_file[j]
                        else:
                            ff+=current_file[j]
        
                if cnt and cnt not in contents:
                    contents[cnt]=[root+"/"+ff]
                else:
                    if cnt:
                        contents[cnt].append(root+"/"+ff)
        ans=[]
        for lis in contents:
            if len(contents[lis])>=2:
                ans.append(contents[lis])
        return ans

                    
        



