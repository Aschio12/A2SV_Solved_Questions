class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        summ,found=0,False
        skill.sort()
        l,r=0,len(skill)-1
        prod=0
        while l<r:
            if not found:
                summ=skill[l]+skill[r]
                found=not found
                prod+=(skill[l]*skill[r])
            else:
                if skill[l]+skill[r]!=summ:
                    return -1
                else:
                    prod+=(skill[l]*skill[r])
            l+=1
            r-=1
        return prod

            

        