class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count=defaultdict(int)
        for cpd in cpdomains:
            v_dom=cpd.split()
            visit=int(v_dom[0])
            domain=v_dom[1].split(".")
            for i in range(len(domain)-1):
                current=domain[i]+"."
                for k in range(i+1,len(domain)-1):
                    current+=domain[k]+"."
                count[current+domain[-1]]+=visit
            count[domain[-1]]+=visit
        ans=[]
        for dom,v in count.items():
            ans.append(f"{v} {dom}")
        return ans



