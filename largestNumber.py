class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new_str=[str(num) for num in nums]
        new_str.sort(key=lambda x: x*10,reverse=True)
        return "".join(new_str) if new_str[0]!="0" else "0"