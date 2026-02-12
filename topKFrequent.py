class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store=[]
        counter=defaultdict(int)
        for num in nums:
            counter[num]+=1

        for key,val in counter.items():
            store.append((val,key))
        store.sort(reverse=True)
        ans=[]
        for i in range(k):
            ans.append(store[i][1])
        return ans

            

        