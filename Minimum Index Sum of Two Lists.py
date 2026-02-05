class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list11,list22=[],[]
        for i in range(len(list1)):
            list11.append((list1[i],i))
        for j in range(len(list2)):
            list22.append((list2[j],j))
        list11.sort()
        list22.sort()
        l1,l2=0,0
        d={}
        m=2002
        while l1<len(list11) and l2<len(list22):
            if list11[l1][0]==list22[l2][0]:
                m=min(m,list11[l1][1]+list22[l2][1])
                d[list11[l1][0]]=list11[l1][1]+list22[l2][1]
                l2+=1
                l1+=1
            elif list11[l1][0]>list22[l2][0]:
                l2+=1
            else:
                l1+=1
        ans=[]
        for key,val in d.items():
            if val==m:
                ans.append(key)
        return ans


