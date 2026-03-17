class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        ans=0
        for key,val in c.items():
            curr_member=key+1
            c_group=(key+val)//curr_member
            ans+=curr_member*c_group
        return ans

        