class Solution:
    def frequencySort(self, s: str) -> str:
        ss=Counter(s)
        store=[]
        for key,val in ss.items():
            store.append([val,key])
        store.sort(reverse=True)
        ans=""
        for reps,c in store:
            for i in range(reps):
                ans+=c
        return ans