class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        left=[1]* len(arr)
        right=[1]* len(arr)
        bl=1
        br=1
        for i in range(len(left)):
            left[i]=bl
            bl*=arr[i]
        for i in range(len(right)-1,-1,-1):
            right[i]=br
            br*=arr[i]
        ans=[]
        for i in range(len(arr)):
            ans.append(left[i]*right[i])
        return(ans)