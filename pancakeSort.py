class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n,ans=len(arr),[]
        for i in range(len(arr)):
            max_el_index=arr.index(max(arr[:n-i]))+1
            arr[:max_el_index]= arr[:max_el_index][::-1]
            ans.append(max_el_index)
            ans.append(n-i)
            arr[:n-i]= arr[:n-i][::-1]
        return ans
