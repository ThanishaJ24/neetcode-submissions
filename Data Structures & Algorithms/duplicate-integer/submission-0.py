class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r=defaultdict(int)
        for i in nums:
            r[i]+=1
        
        for key,value in r.items():
            if value >1:
                return True
        return False