class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mark=[0]*len(nums)
        for start,end in requests:
            mark[start]+=1
            if end<len(nums)-1:
                mark[end+1]-=1

        p=0
        for i in range(len(mark)):
            p+=mark[i]
            mark[i]=p

        store=[]
        permu=[0]*len(nums)
        for index,val in enumerate(mark):
            store.append([val,index])
        
        nums.sort(reverse=True)

        store.sort(key=lambda x:x[0], reverse=True)
        for i in range(len(nums)):
            permu[store[i][1]] = nums[i]
        
        p=0
        for i in range(len(permu)):
            p+=permu[i]
            permu[i]=p
        ans=0
        
        for start,end in requests:
            if start>0:
                ans+=permu[end]-permu[start-1]
            else:
                ans+=permu[end]
        
        return ans%(10**9 + 7)

        


