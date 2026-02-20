class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d=Counter(s)
        start,right="",""
        ss=set(s)
        for i in range(len(order)):
            if order[i] in d:
                start+=(order[i]*d[order[i]])

        for ch in ss:
            if ch not in order:
                right+=(ch*d[ch])
        return start+right
        