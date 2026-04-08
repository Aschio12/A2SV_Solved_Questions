class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket=[[] for i in range(len(nums)+1)]
        d=Counter(nums)

        ind=0
        for val,reps in d.items():
            bucket[reps].append(val)
            ind=max(ind,reps)

        ans=[]
        for i in range(ind,-1,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
