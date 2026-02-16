class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d=defaultdict(list)
        for index,val in enumerate(nums):
            d[val].append(index)
        count=0
        for num,indexes in d.items():
            if len(indexes)>1:
                for i in range(len(indexes)):
                    for j in range(i+1,len(indexes)):
                        if (indexes[i]*indexes[j])%k==0:
                            count+=1
        return count